from flask import Flask, render_template, request
from flask import jsonify
from utils.electorateData import citySearch
from utils.ageComparison import ageComparisonYoung, ageComparisonSenior
from utils.incomeComparison import incomeComparison
from utils.evolutionComparison import evolutionComparison
from flask import Flask
from flask_cors import CORS
from os import walk
import datetime
import numpy as np

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    # página inicial
    return render_template('index.html')


@app.route('/project')
def project():
    # página sobre o projeto
    return render_template('project.html')


@app.route('/about-us')
def about():
    # página sobre nós
    return render_template('about-us.html')


@app.route('/search-region')
def regions():
    # página de comparação entre regiões
    return render_template('regions.html')


@app.route('/data')
def searchData():
    # armazenamento dos resultados da busca

    # capturando os parâmetros para a busca
    city = request.args.get('city')
    role = request.args.get('role')
    year = request.args.get('year')
    print(f'Cidade: {city}, ano: {year}, cargo: {role}')

    # apontando o arquivo para a busca (buscando o caminho)
    pathData = ''
    for path, _, files in walk('..\jupyter-notebooks\data'):
        pathData = str(path)

    csvPaths = []
    csvPaths.append(pathData + f"\perfil_eleitorado_{year}.csv")
    csvPaths.append(pathData + f"\perfil_comparecimento_abstencao_{year}.csv")

    # Carrega CSVs do ano eleitoral escolhido
    federal = np.arange(1994, datetime.date.today().year+4, 4).tolist()
    municipal = np.arange(1996, datetime.date.today().year+4, 4).tolist()

    if int(year) in federal:
        csvPaths.append(pathData + f'\consulta_cand_{year}_BRASIL.csv')
    elif int(year) in municipal:
        csvPaths.append(pathData + f'\consulta_cand_{year}_SP.csv')
    else:
        print("Escolha um ano válido! Volte ao início do notebook, altere o ano e rode aquela e esta célula novamente")

    # executando a busca e retornando o resultado
    result = citySearch(city.upper(), role.upper(), csvPaths)

    return jsonify(result)


@app.route('/data-regions')
def comparisonData():
    # armazenamento dos resultados da comparação

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
    else:
        csvPaths = []
        csvPaths.append(pathData + f"\eleitorado_municipio_2014.csv")
        csvPaths.append(pathData + f"\eleitorado_municipio_2016.csv")
        csvPaths.append(pathData + f"\eleitorado_municipio_2018.csv")
        csvPaths.append(pathData + f"\eleitorado_municipio_2020.csv")

        if year == 2022:
            csvPaths.append(pathData + f"\eleitorado_municipio_2022.csv")
        elif year == 2024:
            csvPaths.append(pathData + f"\eleitorado_municipio_2022.csv")
            csvPaths.append(pathData + f"\eleitorado_municipio_2024.csv")

        result = evolutionComparison(year, csvPaths)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
