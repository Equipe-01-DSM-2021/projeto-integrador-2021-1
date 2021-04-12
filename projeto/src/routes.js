const express = require('express')
const routes = express.Router()
const SearchController = require('./controllers/SearchController')

routes.get('/', SearchController.index)
routes.get('/search', SearchController.search)

module.exports = routes;
