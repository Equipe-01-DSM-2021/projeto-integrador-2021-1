import pandas as pd
def SearchForColumn(path, CityToSearch):
    col_list = ["NM_MUNICIPIO", "DS_GENERO","DS_GRAU_ESCOLARIDADE", "DS_FAIXA_ETARIA", "DS_ESTADO_CIVIL"]

    # Lê o csv
    iter_csv = pd.read_csv(
        path, 
        usecols=col_list,
        delimiter=";",
        encoding='iso-8859-1',
        error_bad_lines=False)

    # Remove a coluna da cidade
    df_result = iter_csv.loc[iter_csv["NM_MUNICIPIO"] == CityToSearch].drop(columns=["NM_MUNICIPIO"], axis=1)

    # Converte para json
    df_result.apply(pd.Series.value_counts, axis=1)
    



    ds_genero_string = df_result["DS_GENERO"].value_counts().to_json()
    ds_grau_escolaridade_string = df_result["DS_GRAU_ESCOLARIDADE"].value_counts().to_json()
    ds_estado_civil_string = df_result["DS_ESTADO_CIVIL"].value_counts().to_json()

    ds_faixa_etaria_string = df_result["DS_FAIXA_ETARIA"].value_counts().to_json()
    ds_faixa_etaria_string = ds_faixa_etaria_string.replace("  ", "")

    string_completa = '{' + f'"DS_GENERO": {ds_genero_string}, "DS_GRAU_ESCOLARIDADE": {ds_grau_escolaridade_string}, "DS_ESTADO_CIVIL": {ds_estado_civil_string}, "DS_FAIXA_ETARIA": {ds_faixa_etaria_string}' + '}' 
    print(string_completa)



# Exemplo
path = "perfil_eleitorado_2020.csv"
df = SearchForColumn(path, "SÃO PAULO")


