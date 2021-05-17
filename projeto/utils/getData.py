import pandas as pd


def SearchForColumn(path, columnToSearch, city):
    # realizando a busca
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
                             city].drop(columns=["NM_MUNICIPIO"], axis=1)

    # Converte para dicionário
    df_result = df_result.value_counts().to_json()

    # Remove os erros
    df_result = df_result.replace("(", "")
    df_result = df_result.replace(")", "")
    df_result = df_result.replace("   ", "")
    df_result = df_result.replace(",',)", "")
    df_result = df_result.replace(',":', '":')
    df_result = df_result.replace("'", "")

    print(df_result)

    return df_result
