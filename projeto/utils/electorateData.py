import pandas as pd


def citySearch(city, role, csvPaths):
    # CARACTERÍSTICAS GERAIS DO ELEITORADO
    col_list_electorate = ["NM_MUNICIPIO", "DS_GRAU_ESCOLARIDADE",
                           "QT_ELEITORES_INC_NM_SOCIAL", "DS_FAIXA_ETARIA",
                           "DS_ESTADO_CIVIL"]

    iter_csv_electorate = pd.read_csv(csvPaths[0], usecols=col_list_electorate,
                                      delimiter=";", encoding='iso-8859-1',
                                      error_bad_lines=False)

    # Remove a coluna da cidade
    df_result = iter_csv_electorate.loc[iter_csv_electorate["NM_MUNICIPIO"] == city].drop(
        columns=["NM_MUNICIPIO"], axis=1)

    # Converte para json
    df_result.apply(pd.Series.value_counts, axis=1)

    # capturando os dados
    electorate = electorate_data(df_result, city)
    social_name = social_name_data(df_result)

    # CANDIDATO ELEITO
    # Geração do CSV de candidato
    col_list_candidate = ["NR_TURNO", "NM_UE", "DS_CARGO",
                          "NM_CANDIDATO", "SG_PARTIDO",
                          "DS_SIT_TOT_TURNO"]

    iter_csv_candidate = pd.read_csv(csvPaths[2], usecols=col_list_candidate,
                                     sep=';', encoding='iso-8859-1',
                                     error_bad_lines=False)

    # capturando os dados
    candidate = elected_candidate_data(iter_csv_candidate, city, role)

    # COMPARECIMENTO E ABSTENÇÃO
    col_list_attendance_abstention = ["NR_TURNO", "NM_MUNICIPIO",
                                      "QT_APTOS", "QT_COMPARECIMENTO", "QT_ABSTENCAO"]

    iter_csv_attendance_abstention = pd.read_csv(csvPaths[1],
                                                 usecols=col_list_attendance_abstention,
                                                 sep=';',
                                                 encoding='iso-8859-1',
                                                 error_bad_lines=False)

    # capturando os dados
    attendance_abstention = attendance_abstention_data(
        iter_csv_attendance_abstention, city)

    cards = '{ "cards": [' + electorate + '], "cardCandidato": [' + \
        candidate + '], "cardNomeSocial": [{' + social_name + \
        '}], "cardComparecimento": [' + attendance_abstention + ']}'

    print(cards)
    return cards


def electorate_data(df_result, city):
    schooling = df_result["DS_GRAU_ESCOLARIDADE"].value_counts(
    ).to_json()

    marital_status = df_result["DS_ESTADO_CIVIL"].value_counts()
    marital_status = marital_status[:-1].to_json()

    age_group = df_result["DS_FAIXA_ETARIA"].value_counts(
    ).to_json()

    age_group = age_group.replace("  ", "")

    electorate_cards = '{' + f'"DS_GRAU_ESCOLARIDADE": {schooling}, "DS_ESTADO_CIVIL": {marital_status}, "DS_FAIXA_ETARIA": {age_group}' + '}'

    electorate = electorate_cards.replace(
        '\n', ' ').replace('\r', '')

    return electorate


def social_name_data(df_result):
    # NOME SOCIAL
    social_name_total = 0  # Iniciando a variável
    df_social_name = df_result.groupby('QT_ELEITORES_INC_NM_SOCIAL')[
        'QT_ELEITORES_INC_NM_SOCIAL'].sum()

    # Somando a quantidade de eleitores com nome social em cada grupo
    for index_social_name in range(len(df_social_name)):
        social_name_total += df_social_name.index[index_social_name] * \
            df_social_name.values[index_social_name]

    amount = str(social_name_total)
    # Gerando string do nome social
    social_name = f'"quantidade": {amount}'

    return social_name


def elected_candidate_data(iter_csv, city, role):
    # função para buscar os dados do candidato eleito

    # Verificando cargo desejado e criando query a partir disso
    if role == "GOVERNADOR":
        candidate = iter_csv.query(
            f'DS_CARGO == "{role}" and DS_SIT_TOT_TURNO == "ELEITO" and NM_UE == "SÃO PAULO"')

    elif role == "PREFEITO":
        candidate = iter_csv.query(
            f'DS_CARGO == "{role}" and DS_SIT_TOT_TURNO == "ELEITO" and NM_UE == "{city}"')

    else:
        candidate = iter_csv.query(
            f'DS_CARGO == "{role}" and DS_SIT_TOT_TURNO == "ELEITO"')

    candidate_result = candidate.drop(
        columns=["NM_UE"], axis=1).reset_index(drop=True)
    candidate_result = candidate_result.drop(
        columns=["DS_SIT_TOT_TURNO"], axis=1).squeeze().to_json()

    return candidate_result


def attendance_abstention_data(iter_csv, city):
    # função para buscar os dados sobre comparecimento e abstenção

    abstention_city = iter_csv.query(f'NM_MUNICIPIO == "{city.upper()}"')

    # Avaliando abstenções no primeiro turno
    first_round_data = abstention_city.query('NR_TURNO == 1')
    attendance_first_round = first_round_data.QT_COMPARECIMENTO.sum()
    abstention_first_round = first_round_data.QT_ABSTENCAO.sum()

    # Avaliando abstenções no segundo turno
    second_round_data = abstention_city.query('NR_TURNO == 2')
    attendance_second_round = second_round_data.QT_COMPARECIMENTO.sum()
    abstention_second_round = second_round_data.QT_ABSTENCAO.sum()

    attendance_abstention_result = '{"comparecimento_primeiro_turno": ' + str(
        attendance_first_round) + ',"abstencao_primeiro_turno":' + str(abstention_first_round) + \
        '}, {"comparecimento_segundo_turno": ' + str(attendance_second_round) + \
        ', "abstencao_segundo_turno":' + str(abstention_second_round) + '}'

    return attendance_abstention_result
