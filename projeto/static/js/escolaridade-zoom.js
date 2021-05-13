var ctx = document.getElementById('gz-escolaridade').getContext('2d');

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Analfabeto', 'Lê e escreve', 'Fundamental completo', 'Fundamental incompleto', 'Médio completo', 'Médio incompleto', 'Superior completo', 'Superior incompleto'],
        datasets: [{
            label: 'Total',
            data: [33, 33, 43, 33, 35, 33, 23, 31],
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
        },
    }
});