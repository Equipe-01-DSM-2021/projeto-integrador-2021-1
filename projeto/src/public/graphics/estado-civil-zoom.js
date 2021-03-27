var ctx = document.getElementById('gz-estado-civil').getContext('2d');

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Solteiro', 'Casado', 'Viúvo', 'Sep. judicialmente', 'Divorciado'],
        datasets: [{
            label: 'Total',
            data: [34, 44, 54, 44, 44],
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