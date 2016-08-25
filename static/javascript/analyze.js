"user strict";

var options = { responsive: true };

var ctx_donut = $("#donutChart").get(0).getContext("2d");
var ctx_bar = $("#barChart").get(0).getContext("2d");
var ctx_line = $("#lineChart").get(0).getContext("2d");

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

// Make bar graph of number of protests in specific countries 
function makeBar(){
    var month = $("#month").val();
    var day = $("#day").val();
    $.get('/eventcode/' + '2016' + month + day + '.json', function (data) {
        var myBarChart = new Chart(ctx_bar, {
                                            type: 'bar',
                                            data: data,
                                            options: options
                                          });
        $('#donutLegend').html(myBarChart.generateLegend());
    });
}

// Make line graph of all protests in 2016 
function makeLine(){
    var month = $("#month").val();
    var day = $("#day").val();
    $.get('/eventcode/' + '2016' + month + day + '.json', function (data) {
        var myLineChart = new Chart(ctx_line, {
                                          type: 'line',
                                          data: data,
                                          options: options
                                        });
        $('#donutLegend').html(myLineChart.generateLegend());
    });
}



document.getElementById("submit").addEventListener("click", makeDonut);
document.getElementById("submit").addEventListener("click", makeBar);
document.getElementById("submit").addEventListener("click", makeLine);