"user strict";

var options = { responsive: true };

var ctx_donut = $("#donutChart").get(0).getContext("2d");

// Make donut chart of percentage of different types of events for that day
function makeDonut(){
    var month = $("#month").val();
    var day = $("#day").val();
    $.get('/eventcode/' + '2016' + month + day + '.json', function (data) {
        var myDonutChart = new Chart(ctx_donut, {
                                                type: 'doughnut',
                                                data: data,
                                                options: options
                                              });
        $('#donutLegend').html(myDonutChart.generateLegend());
    });
}

document.getElementById("submit").addEventListener("click", makeDonut);