/* Chamadas de funções e controle de funcionalidades que cada rota representa */

module.exports = {
    index(req, res) {
        //retorna a tela inicial
        return res.render('index')
    },

    search(req, res) {
        //captura os filros enviados pelo botão do form
        const region = req.query.region
        const city = req.query.city
        const role = req.query.role 
        const year = req.query.year

        /* TESTE */
        //retorna um JSON para o front com os filtros capturados
        return res.json({
            region: region, 
            city: city, 
            role: role,
            year: year
        })
    }    
}