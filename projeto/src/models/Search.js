/* Funções que mexem com dados (buscar, cadastrar, atualizar, excluir) */

/* Dados dos CARDS */
const cards = [
  {
    id: 1,
    canvasId: "g-rep-eleito",
    scriptGraphic: "../src/",
    title: "Representante eleito",
    description: "Legendas e descrição",
    zoomGraphic: "../static/rep-eleito-zoom.js",
  },
  {
    id: 2,
    canvasId: "g-escolaridade",
    scriptGraphic: "../static/escolaridade-graphic.js",
    title: "Escolaridade",
    description: "Legendas e descrição",
    zoomGraphic: "../static/escolaridade-zoom.js",
  },
  {
    id: 3,
    canvasId: "g-genero",
    scriptGraphic: "../static/genero-graphic.js",
    title: "Gênero",
    description: "Legendas e descrição",
    zoomGraphic: "../static/genero-zoom.js",
  },
  {
    id: 4,
    canvasId: "g-estado-civil",
    scriptGraphic: "../static/estado-civil-graphic.js",
    title: "Estado civil",
    description: "Legendas e descrição",
    zoomGraphic: "../static/estado-civil-zoom.js",
  },
  {
    id: 5,
    canvasId: "g-nomsocial-def",
    scriptGraphic: "../static/nomsocial-def-graphic.js",
    title: "Possuintes de nome social ou deficiência",
    description: "Legendas e descrição",
    zoomGraphic: "../static/nomsocial-def-zoom.js",
  },
  {
    id: 6,
    canvasId: "g-faixa-etaria",
    scriptGraphic: "../static/faixa-etaria-graphic.js",
    title: "Faixa etária",
    description: "Legendas e descrição",
    zoomGraphic: "../static/faixa-etaria-zoom.js",
  },
];

/* Funções para exportações de dados */
module.exports = {
  /* Função que retorna os valores dos CARDS */
  enableCards() {
    return cards;
  },
};
