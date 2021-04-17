/* Config. global do gráfico que deixa a cor dos numeros do eixo y brancas (#ffff) */
Chart.defaults.global.defaultFontColor = "#ffff";

var ctx = document.getElementById('g-faixa-etaria').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['16 a 18 anos', '19 a 29 anos', '30 a 49 anos', '50 a 59 anos', '60 anos ou mais'],
        datasets: [{
            label: 'Total',
            data: [54,52,42,52,62],
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
                }
            }],
            /* Retira os valores do eixo X da exibição */
            xAxes: [{
                display: false,
            }]
        },
    }
});