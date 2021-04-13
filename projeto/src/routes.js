//"importação" de funções e arquivos necessários para o funcionamento das rotas
const express = require('express')
const routes = express.Router()
const SearchController = require('./controllers/SearchController')

//início (tela principal)
routes.get('/', SearchController.index)
//resultado da busca (tela com as estatíticas)
routes.get('/search', SearchController.search)

module.exports = routes;
