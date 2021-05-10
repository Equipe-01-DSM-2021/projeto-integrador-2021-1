/* Funções que mexem com dados (buscar, cadastrar, atualizar, excluir) */
const { spawn } = require("child_process");

/* Dados dos CARDS */
const cards = [
  {
    id: 1,
    canvasId: "g-rep-eleito",
    title: "Representante eleito",
    description: "Legendas e descrição",
    /* DADOS DO GRÁFICO */
    labels: ["Fulano", "Ciclano", "Beltrano"],
    data: [46, 134, 88],
  },
  {
    id: 2,
    canvasId: "g-escolaridade",
    title: "Escolaridade",
    description: "Legendas e descrição",
    /* DADOS DO GRÁFICO */
    labels: [
      "Analfabeto",
      "Lê e escreve",
      "Fundamental completo",
      "Fundamental incompleto",
      "Médio completo",
      "Médio incompleto",
      "Superior completo",
      "Superior incompleto",
    ],
    data: [33, 33, 43, 33, 35, 33, 23, 31],
  },
  {
    id: 3,
    canvasId: "g-genero",
    title: "Gênero",
    description: "Legendas e descrição",
    /* DADOS DO GRÁFICO */
    labels: ["Feminino", "Masculino"],
    data: [100, 97],
  },
  {
    id: 4,
    canvasId: "g-estado-civil",
    title: "Estado civil",
    description: "Legendas e descrição",
    /* DADOS DO GRÁFICO */
    labels: [
      "Solteiro",
      "Casado",
      "Viúvo",
      "Separado judicialmente",
      "Divorciado",
    ],
    data: [34, 44, 54, 44, 44],
  },
  {
    id: 5,
    canvasId: "g-nomsocial-def",
    title: "Possuintes de nome social ou deficiência",
    description: "Legendas e descrição",
    /* DADOS DO GRÁFICO */
    labels: ["Nome social", "Deficiência"],
    data: [54, 34],
  },
  {
    id: 6,
    canvasId: "g-faixa-etaria",
    title: "Faixa etária",
    description: "Legendas e descrição",
    /* DADOS DO GRÁFICO */
    labels: [
      "16 a 18 anos",
      "19 a 29 anos",
      "30 a 49 anos",
      "50 a 59 anos",
      "60 anos ou mais",
    ],
    data: [54, 52, 42, 52, 62],
  },
];

/* Funções para exportações de dados */
module.exports = {
  /* Função que retorna os valores dos CARDS */
  enableCards() {
    return cards;
  },

  /* Função que passa os parâmetros para o script Python e retorna os valores da busca */
  get(region, city, role, year) {
    var dataSearch;

    //passando os filtros da busca
    const python = spawn("python", [
      "Get_Json_Data.py",
      region,
      city,
      role,
      year,
    ]);

    //guardando o resultado da busca
    python.stdout.on("data", function (data) {
      console.log("Buscando dados...");
      dataSearch = JSON.stringify(data);
    });

    //fechando o processo
    python.on("close", (code) => {
      return dataSearch;
    });
  },

  updateCards(dataSearch) {
    //atualizando os dados do card de escolaridade
    cards[1].labels = dataSearch.x;
    cards[1].data = dataSearch.y;
  },
};
