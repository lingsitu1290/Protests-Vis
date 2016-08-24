var options = { responsive: true };

var ctx_donut = $("#donutChart").get(0).getContext("2d");

// grab fullDate from user!!!
// var month; 
// var day;

// Make donut chart of percentage of different types of events for that day
function makeDonut(){
    $.get('/eventcode/' + '20160811' + '.json', function (data) {
        var myDonutChart = new Chart(ctx_donut, {
                                                type: 'doughnut',
                                                data: data,
                                                options: options
                                              });
        $('#donutLegend').html(myDonutChart.generateLegend());
    });
}

makeDonut();
