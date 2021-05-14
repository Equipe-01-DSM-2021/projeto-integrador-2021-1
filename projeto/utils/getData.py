import pandas as pd


def SearchForColumn(path,  columnToSearch, CityToSearch):
    col_list = ["NM_MUNICIPIO", columnToSearch]

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
    df_result = df_result.value_counts().to_json()

    # Formata o json para remover os erros
    df_result = df_result.replace("(", "")
    df_result = df_result.replace(")", "")
    df_result = df_result.replace("   ", "")
    df_result = df_result.replace(",',)", "")
    df_result = df_result.replace(',":', '":')
    df_result = df_result.replace("'", "")

    return df_result


path = 'jupyter-notebooks/data/perfil_eleitorado_2020.csv'

result = SearchForColumn(path, "DS_GRAU_ESCOLARIDADE", "SÃO JOSÉ DOS CAMPOS")
print(result)
