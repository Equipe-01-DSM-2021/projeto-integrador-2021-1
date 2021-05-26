const Modal = {
  toggleZoom(chartCod, chartTitle, labelStringY) {
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

    // criando o gráfico
    Chart.defaults.global.defaultFontColor = "#50525f";
    var ctx = document.getElementById('chart-zoom').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: global.dataKeys[chartCod],
            datasets: [{
                label: 'Total',
                data: global.dataValues[chartCod],
                backgroundColor: 'rgba(154, 219, 249, 0.4)',
                borderColor: 'rgba(154, 219, 249)',
                borderWidth: 1,
            }]
        },
        options: {
            /* Desativa a legenda */
            legend: {
                display: false
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
            }
        }
    });





  },
  toggleHelp() {
    document.querySelector(".modal-overlay-help").classList.toggle("active");
  },
  toggleDownload() {
    document.querySelector(".tooltip").classList.toggle("active");
  },
};
