/* Chamadas de funções e controle de funcionalidades que cada rota representa */

module.exports = {
    index(req, res) {
        return res.render('index')
    },

    search(req, res) {
        const region = req.query.region
        const city = req.query.city
        const role = req.query.role 
        const year = req.query.year

        return res.json({
            region: region, 
            city: city, 
            role: role,
            year: year
        })
    }    
}