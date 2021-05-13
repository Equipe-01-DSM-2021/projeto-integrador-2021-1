from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def proc_dados():
    dados = {'ano_eleicao': '2020', 'votantes': 20000000}
    return jsonify(dados)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
