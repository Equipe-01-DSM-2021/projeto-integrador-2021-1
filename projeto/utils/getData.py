import pandas as pd

# Variaveis para o csv
filename_candidatos = "consulta_cand_2018_BRASIL.csv"
filename_eleitorado = "perfil_eleitorado_2020.csv"
cityToSearch = "SÃO PAULO"

# Geração do CSV de candidato
col_list_candidato = ["NR_TURNO", "NM_UE", "DS_CARGO", 
    "NM_CANDIDATO", "SG_PARTIDO", 
    "DS_SIT_TOT_TURNO", "ST_REELEICAO"]

iter_csv_candidato = pd.read_csv(filename_candidatos, 
    usecols=col_list_candidato,    
    sep=';', 
    encoding='iso-8859-1',
    error_bad_lines=False)


# Geração do CSV do eleitorado
col_list_eleitorado = ["NM_MUNICIPIO", "DS_GENERO","DS_GRAU_ESCOLARIDADE", "QT_ELEITORES_INC_NM_SOCIAL", "DS_FAIXA_ETARIA", "DS_ESTADO_CIVIL"]

iter_csv_eleitorado = pd.read_csv(
    filename_eleitorado, 
    usecols=col_list_eleitorado,
    delimiter=";",
    encoding='iso-8859-1',
    error_bad_lines=False)

# Função para ajeitar a string final do eleitorado
def StringEleitorado(iter_csv, CityToSearch):
    # Remove a coluna da cidade
    df_result = iter_csv.loc[iter_csv["NM_MUNICIPIO"] == CityToSearch].drop(columns=["NM_MUNICIPIO"], axis=1)

    # Converte para json
    df_result.apply(pd.Series.value_counts, axis=1)
    
    # Alterações necessárias
    ds_genero_string = df_result["DS_GENERO"].value_counts().to_json()
    ds_grau_escolaridade_string = df_result["DS_GRAU_ESCOLARIDADE"].value_counts().to_json()
    ds_estado_civil_string = df_result["DS_ESTADO_CIVIL"].value_counts().to_json()

    ds_faixa_etaria_string = df_result["DS_FAIXA_ETARIA"].value_counts().to_json()
    ds_faixa_etaria_string = ds_faixa_etaria_string.replace("  ", "")

    string_completa = '{' + f'"DS_GENERO": {ds_genero_string}, "DS_GRAU_ESCOLARIDADE": {ds_grau_escolaridade_string}, "DS_ESTADO_CIVIL": {ds_estado_civil_string}, "DS_FAIXA_ETARIA": {ds_faixa_etaria_string}' + '}' 
    string_completa = string_completa.replace('\n', ' ').replace('\r', '')
    
    
    return string_completa


# Função para ajeitar a string final do candidato
def StringCandidato(iter_csv):
    
    df_result = iter_csv.query('DS_CARGO == "PRESIDENTE" and DS_SIT_TOT_TURNO == "ELEITO"').to_json()

    return df_result

# Função para ajeitar a string final do nome social do eleitorado
def stringNomeSocial(iter_csv, CityToSearch):

    df_result = iter_csv.loc[iter_csv["NM_MUNICIPIO"] == CityToSearch].drop(columns=["NM_MUNICIPIO"], axis=1)

    total_eleitores_nomesocial = 0 # Iniciando a variável
    df_nomesocial = df_result.groupby('QT_ELEITORES_INC_NM_SOCIAL')['QT_ELEITORES_INC_NM_SOCIAL'].sum()
    
    # Somando a quantidade de eleitores com nome social em cada grupo
    for index_nomesocial in range(len(df_nomesocial)):
        total_eleitores_nomesocial += df_nomesocial.index[index_nomesocial] * df_nomesocial.values[index_nomesocial]

    qntString = str(total_eleitores_nomesocial)
    stringCompleta = f'"quantidade": {qntString}'

    return stringCompleta


# Todos os cards sendo feitos
eleitorado_card = StringEleitorado(iter_csv_eleitorado, cityToSearch)
candidato_card = StringCandidato(iter_csv_candidato)
nomeSocial_card = stringNomeSocial(iter_csv_eleitorado, cityToSearch)

# Cards sendo colocados em uma unica string
stringCompleta = '{ "cards": [' + eleitorado_card + '], "cardsCandidato": [' + candidato_card + '], "cardsNomeSocial": [{' + nomeSocial_card + '}]}'
print(stringCompleta)
