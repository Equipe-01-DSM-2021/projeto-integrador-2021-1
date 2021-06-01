const Modal = {

  // MODAL ZOOM
  toggleZoom(chartCod, chartTitle, labelStringY, chartType, comparison) {
    // Ativação do modal
    document.querySelector(".modal-overlay").classList.toggle("active");

    // adicionando o canvas
    canvas = document.getElementById("canvas");
    canvas.innerHTML = '';
    canvas.innerHTML = '<canvas id="chart-zoom" width="auto" height="auto"></canvas>';

    // configurando o modal
    title = document.getElementById("chartTitle");
    title.innerHTML = chartTitle;
    console.log();

    if (comparison==1) {

      // criando o gráfico
      Chart.plugins.register(ChartDataLabels);
      Chart.defaults.global.defaultFontColor = "#50525f";
      var ctx = document.getElementById('chart-zoom').getContext('2d');
      var myChart = new Chart(ctx, {
        type: chartType,
        data: {
          labels: global.dataKeys[chartCod],
          datasets: [{
              backgroundColor: 'rgba(154, 219, 249, 0.4)',
              borderColor: 'rgba(154, 219, 249)',
              borderWidth: 1,
              data: global.dataValues[chartCod],
              datalabels: {
                align: 'bottom',
                anchor: 'end'
              }
          }]
        },
        options: {
          legend: {
            display: false
          },
          plugins: {
            datalabels: {
              color: '#50525f',
              // Porcentagem
              formatter: (value, ctx) => {
                return Math.round(global.dataPorcentage[chartCod][ctx.dataIndex] * 100) + '% do eleitorado da região';
              }
            }
          },
          scales: {
            xAxes: [{
              stacked: true
            }],
            yAxes: [{
                stacked: true,
                ticks: {
                    beginAtZero: true
                },
                scaleLabel: {
                  display: true,
                  labelString: labelStringY
                }
            }]
          }
        }
      });
    } else {

      Chart.defaults.global.defaultFontColor = "#50525f";
      var ctx = document.getElementById('chart-zoom').getContext('2d');
      var myChart = new Chart(ctx, {
          type: chartType,
          data: {
              labels: global.dataKeys[chartCod],
              datasets: [{
                  data: global.dataValues[chartCod],
                  backgroundColor: 'rgba(154, 219, 249, 0.4)',
                  borderColor: 'rgba(154, 219, 249)',
                  borderWidth: 1,
                  datalabels: {
                    align: '',
                    anchor: ''
                  }
              }]
          },
          options: {
              //  Desativa a legenda
              legend: {
                  display: false
              },
              plugins: {
                datalabels: {
                  color: '',
                  font: {},
                  formatter: {}
                }
              },
              scales: {
                  yAxes: [{
                      ticks: {
                          beginAtZero: true
                      },
                      scaleLabel: {
                        display: true,
                        labelString: labelStringY
                      }
                  }]
              },
          }
      });
    }
  },

  // MODAL DOWNLOAD
  toggleDownload() {
    document.querySelector(".tooltip").classList.toggle("active");
  },
};
