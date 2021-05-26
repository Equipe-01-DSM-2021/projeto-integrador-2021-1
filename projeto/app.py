from flask import Flask, render_template, request
from flask import jsonify
from utils.getData import SearchForColumn
from utils.ageData import ageComparisonYoung, ageComparisonSenior, incomeComparison
from flask import Flask
from flask_cors import CORS
from os import walk

app = Flask(__name__)
CORS(app)

# página inicial


@app.route('/')
def index():
    return render_template('index.html')

# página sobre o projeto


@app.route('/project')
def project():
    return render_template('project.html')

# página sobre nós


@app.route('/about-us')
def about():
    return render_template('about-us.html')

# página de comparação entre regiões


@app.route('/search-region')
def regions():
    return render_template('regions.html')

# rota para armazenar os resultados da busca


@app.route('/data')
def searchData():
    # capturando os parâmetros para a busca
    city = request.args.get('city')
    role = request.args.get('role')
    year = request.args.get('year')
    print(f'Cidade: {city}, ano: {year}')

    # apontando o arquivo para a busca (buscando o caminho)
    pathData = ''
    for path, _, files in walk('..\jupyter-notebooks\data'):
        pathData = str(path)

    csvPath = pathData + f"\perfil_eleitorado_{year}.csv"

    # executando a busca e retornando o resultado
    result = SearchForColumn(csvPath, city.upper())

    return jsonify(result)


@app.route('/data-regions')
def comparisonData():
    # capturando os parâmetros para a busca
    comparison = request.args.get('comparison')
    year = request.args.get('year')
    print(f'Ano: {year}, {comparison}')

    # apontando o arquivo para a busca (buscando o caminho)
    pathData = ''
    for path, _, files in walk('..\jupyter-notebooks\data'):
        pathData = str(path)

    csvPath = pathData + f"\perfil_eleitorado_{year}.csv"

    # executando a busca e retornando o resultado
    if comparison == 'jovens':
        result = ageComparisonYoung(year, csvPath)
    elif comparison == 'idosos':
        result = ageComparisonSenior(year, csvPath)
    elif comparison == 'renda':
        csvPath = pathData + f"\cadastro_central_de_empresas.csv"
        result = incomeComparison(csvPath)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
