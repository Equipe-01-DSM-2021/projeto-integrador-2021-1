from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)


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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def searchData():
    print('cheguei')
    # capturando os parâmetros para a busca
    city = request.args.get('city')
    role = request.args.get('role')
    year = request.args.get('year')
    print(f'Cidade: {city}, ano: {year}')

    # apontando o arquivo para a busca
    path = f'perfil_eleitorado_{year}.csv'

    # executando a busca e retornando o resultado
    result = SearchForColumn(path, "DS_GRAU_ESCOLARIDADE", city.upper())
    print(result)
    print(type(result))

    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
