const express = require('express')
const server = express()
const routes = require('./routes')
const path = require('path')

server.set('view engine', 'ejs')

//mudar a localização da pasta views
server.set('views', path.join(__dirname, 'views'))

// habilita arquivos estáticos
server.use(express.static('public'))

//usar o req.body
server.use(express.urlencoded({ extended: true }))

//rotas
server.use(routes)

server.listen(3000, () => console.log('servidor ativo'))