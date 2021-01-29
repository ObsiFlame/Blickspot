let myChart = document.getElementById('myChart').getContext('2d');

// Global Options

Chart.defaults.global.defaultFontFamily = 'Google-Product-Sans-Regular'; 
Chart.defaults.global.defaultFontSize = 15;

let AttacksChart = new Chart(myChart,{
    type:'line', // bar , horizontal bar, radar
    data:{
        labels:['Malware', 'DDoS', 'Phishing', 'Botnets', 'MITM', 'Spyware'],
        datasets:[{
            label:'Number of Attacks',
            data:[
                734,
                2373,
                600,
                2200,
                1200,
                500
            ],
            backgroundColor:[
                '#5851DB',
                '#C13584',
                '#833AB4',
                '#FD1D1D',
                '#EE7762',
                '#FFDC80'
            ],
            borderWidth:3,
            borderColor:'#f73660',
            fill:false,
            pointRadius:6
        }]

    },
    options:{
        scales: {
            xAxes: [{
                ticks: {
                    padding:2
                }
            }]
        }
    }
})