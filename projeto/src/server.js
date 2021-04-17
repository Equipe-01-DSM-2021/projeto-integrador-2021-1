//"importação" de funções e arquivos necessários para o funcionamento do servidor
const express = require('express')
const server = express()
const routes = require('./routes')
const path = require('path')

//configuração da template engine utilizada no projeto
server.set('view engine', 'ejs')

//configuração da localização da pasta views
server.set('views', path.join(__dirname, 'views/templates'))

//habilita arquivos estáticos (imagens, estilos, scripts de interação...)
server.use(express.static('public'))

//habilita uso do req.body (para obter informações do corpo da requisição - respostas do form)
server.use(express.urlencoded({ extended: true }))

//habilita o uso das rotas criadas
server.use(routes)

//configuração do servidor para usar a porta 3000
server.listen(3000, () => console.log('servidor ativo'))