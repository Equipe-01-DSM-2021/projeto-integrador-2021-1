import pandas as pd


def SearchForColumn(path, CityToSearch):
    col_list = ["NM_MUNICIPIO", "DS_GRAU_ESCOLARIDADE",
                "DS_FAIXA_ETARIA", "DS_ESTADO_CIVIL"]

    # Lê o csv
    iter_csv = pd.read_csv(
        path,
        usecols=col_list,
        delimiter=";",
        encoding='iso-8859-1',
        error_bad_lines=False)

    # Remove a coluna da cidade
    df_result = iter_csv.loc[iter_csv["NM_MUNICIPIO"] ==
                             CityToSearch].drop(columns=["NM_MUNICIPIO"], axis=1)

    # Converte para json
    df_result.apply(pd.Series.value_counts, axis=1)

    ds_grau_escolaridade_string = df_result["DS_GRAU_ESCOLARIDADE"].value_counts(
    ).to_json()
    ds_estado_civil_string = df_result["DS_ESTADO_CIVIL"].value_counts(
    ).to_json()

    ds_faixa_etaria_string = df_result["DS_FAIXA_ETARIA"].value_counts(
    ).to_json()
    ds_faixa_etaria_string = ds_faixa_etaria_string.replace("  ", "")

    # Cria a string do json
    # Estrutura:
    # {
    #   "cards": [
    #       dados do grau de escolaridade (Ex.: {"Analfabeto":200})
    #       dados do estado civil (Ex.: {"Solteiro":200})
    #       dados da faixa etária (Ex.: {"18 anos":200})
    #   ]
    # }

    string_completa = '{ "cards": [ ' + ds_grau_escolaridade_string + \
        ', ' + ds_estado_civil_string + ', ' + ds_faixa_etaria_string + ' ] }'

    # Exibe os dados no console
    print(string_completa)

    # Retorna a string do json
    return string_completa
