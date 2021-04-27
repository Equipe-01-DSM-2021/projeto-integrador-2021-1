/* Chamadas de funções e controle de funcionalidades que cada rota representa */

const Search = require("../models/Search");

module.exports = {
  index(response) {
    /* retorna a tela inicial */
    return response.render("index");
  },

  search(request, response) {
    /*
     * captura dos filtros enviados pelo form e
     * envio para função que realiza a busca na base de dados
     */
    const filters = {
      region: String(request.query.region),
      city: String(request.query.city),
      role: String(request.query.role),
      year: Number(request.query.year),
    };

    const Cards = Search.enableCards();

    /* retorna o template com os dados dos cards que serão exibidos */
    return response.render("index", { cards: Cards });
  },
};
