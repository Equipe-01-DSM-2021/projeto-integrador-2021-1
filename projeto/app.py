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
    response = []

    if checkFileExistance(pathData + f"\perfil_eleitorado_{year}.csv"):
        csvPaths.append(pathData + f"\perfil_eleitorado_{year}.csv")
    else:
        response.append(f"Perfil do eleitorado de {year}")

    if checkFileExistance(pathData + f"\perfil_comparecimento_abstencao_{year}.csv"):
        csvPaths.append(
            pathData + f"\perfil_comparecimento_abstencao_{year}.csv")
    else:
        response.append(f"Comparecimento e abstenção de {year}")

    # Carrega CSVs do ano eleitoral escolhido
    federal = np.arange(1994, datetime.date.today().year+4, 4).tolist()
    municipal = np.arange(1996, datetime.date.today().year+4, 4).tolist()

    if int(year) in federal:
        if checkFileExistance(pathData + f"\consulta_cand_{year}_BRASIL.csv"):
            csvPaths.append(pathData + f"\consulta_cand_{year}_BRASIL.csv")
        else:
            response.append(f"Candidatos de {year}")

    if int(year) in municipal:
        if checkFileExistance(pathData + f"\consulta_cand_{year}_SP.csv"):
            csvPaths.append(pathData + f"\consulta_cand_{year}_SP.csv")
        else:
            response.append(f"Candidatos de {year}")

    if len(response) == 0:
        # executando a busca e retornando o resultado
        result = citySearch(city.upper(), role.upper(), csvPaths)
        return jsonify(result)
    else:
        return jsonify(response)


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

    # variável que acumula os arquivos que não existem
    response = []

    # executando a busca e retornando o resultado
    if comparison == 'jovens':
        csvPath = pathData + f"\perfil_eleitorado_{year}.csv"
        if checkFileExistance(csvPath):
            result = ageComparisonYoung(year, csvPath)
        else:
            response.append(f"Perfil do eleitorado de {year}")
            return jsonify(response)

    elif comparison == 'idosos':
        csvPath = pathData + f"\perfil_eleitorado_{year}.csv"
        if checkFileExistance(csvPath):
            result = ageComparisonSenior(year, csvPath)
        else:
            response.append(f"Perfil do eleitorado de {year}")
            return jsonify(response)

    elif comparison == 'renda':
        csvPath = pathData + f"\cadastro_central_de_empresas.csv"
        result = incomeComparison(csvPath)
    else:
        csvPaths = []
        csvPaths.append(pathData + f"\eleitorado_municipio_2014.csv")
        csvPaths.append(pathData + f"\eleitorado_municipio_2016.csv")
        csvPaths.append(pathData + f"\eleitorado_municipio_2018.csv")
        csvPaths.append(pathData + f"\eleitorado_municipio_2020.csv")

        result = evolutionComparison(year, csvPaths)
    return jsonify(result)


def checkFileExistance(filePath):
    # função que verifica a existência dos CSVs necessários para a busca
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
