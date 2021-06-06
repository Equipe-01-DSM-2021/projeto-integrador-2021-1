const Modal = {
  // MODAL ZOOM
  toggleZoom(chartCod, chartTitle, labelStringY, chartType, comparison) {
    // Ativação do modal
    document.querySelector(".modal-overlay").classList.toggle("active");

    // adicionando o canvas
    canvas = document.getElementById("canvas");
    canvas.innerHTML = "";
    canvas.innerHTML =
      '<canvas id="chart-zoom" width="90%" height="100%"></canvas>';

    // configurando o modal
    title = document.getElementById("chartTitle");
    title.innerHTML = chartTitle;
    console.log();

    if (comparison == 1) {
      // criando o gráfico
      Chart.plugins.register(ChartDataLabels);
      Chart.defaults.global.defaultFontColor = "#50525f";
      var ctx = document.getElementById("chart-zoom").getContext("2d");
      var myChart = new Chart(ctx, {
        type: chartType,
        data: {
          labels: global.dataKeys[chartCod],
          datasets: [
            {
              backgroundColor: "rgba(154, 219, 249, 0.4)",
              borderColor: "rgba(154, 219, 249)",
              borderWidth: 1,
              data: global.dataValues[chartCod],
              datalabels: {
                align: "bottom",
                anchor: "end",
              },
            },
          ],
        },
        options: {
          legend: {
            display: false,
          },
          plugins: {
            datalabels: {
              color: "#50525f",
              // Porcentagem
              formatter: (value, ctx) => {
                return (
                  Math.round(
                    global.dataPorcentage[chartCod][ctx.dataIndex] * 100
                  ) + "% do eleitorado da região"
                );
              },
            },
          },
          scales: {
            xAxes: [
              {
                stacked: true,
              },
            ],
            yAxes: [
              {
                stacked: true,
                ticks: {
                  beginAtZero: true,
                },
                scaleLabel: {
                  display: true,
                  labelString: labelStringY,
                },
              },
            ],
          },
        },
      });
    } else if (comparison == 0) {
      Chart.defaults.global.defaultFontColor = "#50525f";
      var ctx = document.getElementById("chart-zoom").getContext("2d");
      var myChart = new Chart(ctx, {
        type: chartType,
        data: {
          labels: global.dataKeys[chartCod],
          datasets: [
            {
              data: global.dataValues[chartCod],
              backgroundColor: "rgba(154, 219, 249, 0.4)",
              borderColor: "rgba(154, 219, 249)",
              borderWidth: 1,
              datalabels: {
                align: "",
                anchor: "",
              },
            },
          ],
        },
        options: {
          //  Desativa a legenda
          legend: {
            display: false,
          },
          plugins: {
            datalabels: {
              color: "",
              font: {},
              formatter: {},
            },
          },
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
                scaleLabel: {
                  display: true,
                  labelString: labelStringY,
                },
              },
            ],
          },
        },
      });
    } else {
      Chart.defaults.global.defaultFontColor = "#50525f";
      var ctx = document.getElementById("chart-zoom").getContext("2d");
      var myChart = new Chart(ctx, {
        type: chartType,
        data: {
          labels: ["Comparecimento", "Abstenção"],
          datasets: [
            {
              label: "1 Turno",
              data: global.dataComparecimento[0],
              backgroundColor: "rgba(154, 219, 249, 0.4)",
              borderColor: "rgba(154, 219, 249)",
              borderWidth: 1,
              datalabels: {
                align: "",
                anchor: "",
              },
            },
            {
              label: "2 Turno",
              data: global.dataComparecimento[1],
              backgroundColor: "rgba(192, 192, 192, 0.4)",
              borderColor: "rgba(192, 192, 192)",
              borderWidth: 1,
              datalabels: {
                align: "",
                anchor: "",
              },
            },
          ],
        },
        options: {
          //  Desativa a legenda
          legend: {
            display: true,
          },
          plugins: {
            datalabels: {
              color: "",
              font: {},
              formatter: {},
            },
          },
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
                scaleLabel: {
                  display: true,
                  labelString: labelStringY,
                },
              },
            ],
          },
        },
      });
    }
  },

  // MODAL DOWNLOAD GERAL
  toggleDownload(chartID, dataName) {
    // FUNÇÃO PARA BAIXAR O CSV
    function download(csv) {
      //const blob = new Blob([csv], { type:'text/csv;charset=UTF-8' });
      //const url = window.URL.createObjectURL(blob);
      const url = "data:text/csv;charset=utf-8," + encodeURI(csv);

      const a = document.createElement("a");
      a.setAttribute("hidden", "");
      a.setAttribute("href", url);
      a.setAttribute("download", `${dataName}.csv`);

      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }

    // FUNÇÃO PARA GERAR O CSV
    function create(headers, colums) {
      var csv = [];

      // adicionando headers
      csv.push(headers.join(";"));

      // adicionando colunas
      var valuesColums = [];
      colums.forEach(function (value) {
        valuesColums.push(String(value));
      });
      csv.push(valuesColums.join(";"));

      return csv.join("\n");
    }

    // Recebendo valores
    data = global.dataAll[chartID];
    headers = Object.keys(data);
    colums = Object.values(data);

    // Acionando as funções
    csv = create(headers, colums);
    download(csv);
  },

  // MODAL DOWNLOAD COMPARAÇÃO POR IDADE (o formato do json é diferente)
  toggleDownloadAge(chartID, dataName) {
    // FUNÇÃO PARA BAIXAR O CSV
    function download(csv) {
      //const blob = new Blob([csv], { type:'text/csv;charset=UTF-8' });
      //const url = window.URL.createObjectURL(blob);
      const url = "data:text/csv;charset=utf-8," + encodeURI(csv);

      const a = document.createElement("a");
      a.setAttribute("hidden", "");
      a.setAttribute("href", url);
      a.setAttribute("download", `${dataName}.csv`);

      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }

    // FUNÇÃO PARA GERAR O CSV
    function create(headers, colums, porcentage) {
      var csv = [];

      // adicionando headers
      csv.push(headers.join(";"));

      // adicionando linha do valor absoluto
      var valuesColums = [];
      colums.forEach(function (value) {
        valuesColums.push(String(value));
      });
      csv.push(valuesColums.join(";"));

      // adicionando linha da porcentagem
      var valuesPorcentage = [];
      porcentage.forEach(function (value) {
        valuesPorcentage.push(String(value));
      });
      csv.push(valuesPorcentage.join(";"));

      return csv.join("\n");
    }

    // Recebendo valores
    headers = global.dataKeys[chartID];
    colums = global.dataValues[chartID];
    porcentage = global.dataPorcentage[chartID];

    // Acionando as funções
    csv = create(headers, colums, porcentage);
    download(csv);
  },

  // MODAL DOWNLOAD COMPARECIMENTO ÀS URNAS  (o formato do json é diferente)
  toggleDownloadUrnas(chartID, dataName) {
    // FUNÇÃO PARA BAIXAR O CSV
    function download(csv) {
      //const blob = new Blob([csv], { type:'text/csv;charset=UTF-8' });
      //const url = window.URL.createObjectURL(blob);
      const url = "data:text/csv;charset=utf-8," + encodeURI(csv);

      const a = document.createElement("a");
      a.setAttribute("hidden", "");
      a.setAttribute("href", url);
      a.setAttribute("download", `${dataName}.csv`);

      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }

    // FUNÇÃO PARA GERAR O CSV
    function create(headers, colums) {
      var csv = [];

      // adicionando headers
      csv.push(headers.join(";"));

      // adicionando colunas
      var valuesColums = [];
      colums.forEach(function (value) {
        valuesColums.push(String(value));
      });
      csv.push(valuesColums.join(";"));

      return csv.join("\n");
    }

    // Recebendo valores
    headers = [];
    colums = [];

    Object.keys(global.objComparecimento[0]).forEach(function (key) {
      headers.push(key);
    });

    Object.keys(global.objComparecimento[1]).forEach(function (key) {
      headers.push(key);
    });

    Object.values(global.objComparecimento[0]).forEach(function (value) {
      colums.push(value);
    });

    Object.values(global.objComparecimento[1]).forEach(function (value) {
      colums.push(value);
    });

    console.log(headers);
    console.log(colums);

    // Acionando as funções
    csv = create(headers, colums);
    download(csv);
  },
};
