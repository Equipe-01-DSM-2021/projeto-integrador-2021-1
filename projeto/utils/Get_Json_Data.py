import pandas as pd
import sys
# Função que busca quantidade de cada tipo de valor na determinada coluna
# Exemplo, retornar quantos tem ensino superior completo, quantos tem ensino
# medio completo... Retorna um json com o resultado


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


# Exemplo
path = "jupyter-notebooks\data\perfil_eleitorado_2020.csv"
city = str(sys.argv[1]).upper()

# TODO Quantidade no dataframe


def main(city):
    result = SearchForColumn(path, "DS_GRAU_ESCOLARIDADE", city)
    print(result)


if __name__ == '__main__':
    main()