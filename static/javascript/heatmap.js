"use strict";

function initialize() {

            var center = {lat: 45, lng: 10}

            var map = new google.maps.Map(
                    document.getElementById('map-canvas'),{
                    zoom: 2,
                    minZoom: 2, 
                    center: center,
                    // zoomControl: false,
                    streetViewControl: false,
                    scrollwheel: false
                });

            var infoWindow = new google.maps.InfoWindow({
                width: 150
            });

            // Add Style
            var styles = [
            {
                "featureType": "administrative",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "lightness": 33
                    }
                ]
            },
            {
                "featureType": "landscape",
                "elementType": "all",
                "stylers": [
                    {
                        "color": "#f2e5d4"
                    }
                ]
            },
            {
                "featureType": "poi.park",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#c5dac6"
                    }
                ]
            },
            {
                "featureType": "poi.park",
                "elementType": "labels",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "lightness": 20
                    }
                ]
            },
            {
                "featureType": "road",
                "elementType": "all",
                "stylers": [
                    {
                        "lightness": 20
                    }
                ]
            },
            {
                "featureType": "road.highway",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#c5c6c6"
                    }
                ]
            },
            {
                "featureType": "road.arterial",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#e4d7c6"
                    }
                ]
            },
            {
                "featureType": "road.local",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#fbfaf7"
                    }
                ]
            },
            {
                "featureType": "water",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "on"
                    },
                    {
                        "color": "#acbcc9"
                    }
                ]
            }
        ];

            var styledMapOptions = {
              name: 'Custom Style'
            };

            var customMapType = new google.maps.StyledMapType(
                    styles,
                    styledMapOptions);

            map.mapTypes.set('map_style', customMapType);
            map.setMapTypeId('map_style');

// get list of dates
function getListOfDates(){
    var arrayOfDates = [];
    $.get('/events', function (events){
        var events;
        // var arrayOfDates = [];

        for (var key in events) {
            var one_event = events[key]

            arrayOfDates.push(parseInt(one_event.fullDate));
    }
    console.log(arrayOfDates)

});
    // console.log(Array.isArray(arrayOfDates))
    return arrayOfDates;
}

getListOfDates();

/* Add Slider */ 

function createSlider(){
    var sliderDate = [20160801,20160802,20160803,20160804,20160805,20160806,20160807, 20160808,20160809,20160810,20160811,20160812,20160813,20160814,20160815,20160816, 20160817, 20160818]
    $("#slider-1").slider({
        min: sliderDate[0],
        max: sliderDate[sliderDate.length-1],
        step: 1,
        // value: fullDate,
        slide: function(event, ui){
            $('#slider-value2').val(sliderDate[ui.value]);
            // $('#slider-value2').html(sliderDate[ui.value]);
        },
        change: function( event, ui ) {
            // console.log(ui.value)
            // value: $("#slider-1").slider( "option", "value", ui.value);
            $('#slider-value').html(ui.value); 
            //calls changeMap everytime the slider is moved
            changeMap(ui.value);
        },   
    });
    // set the initial environments of the map
    $("#slider-1").slider({
        value: sliderDate[0],
    })
};

createSlider();

// Retrieving events information with AJAX
function changeMap(fullDate){
    $.get('/events/' + fullDate + '.json', function (events) {
        var events, marker, html;

        //Object that stores the lat/ long and the count of the same 
        var arrayOffullDate = [];

        for (var key in events) {
            var one_event = events[key]

            // Define the markers
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(one_event.latitude, one_event.longitude),
                map: map,
                opacity: 0.8,
            });

            // Define the content of the infoWindow
            html = (
                '<div class="window-content">' +
                    '<a target="_blank" href='+ one_event.url + '>' + one_event.url + '</a>' +
                '</div>');

            // Inside the loop we call bindInfoWindow passing it the marker,
            // map, infoWindow and contentString
            bindInfoWindow(marker, map, infoWindow, html);
        }

        });
    };

// This function is outside the for loop.
// When a marker is clicked it closes any currently open infowindows
// Sets the content for the new marker with the content passed through
// then it open the infoWindow with the new content on the marker that's clicked
function bindInfoWindow(marker, map, infoWindow, html) {
  google.maps.event.addListener(marker, 'click', function () {
      infoWindow.close();
      infoWindow.setContent(html);
      infoWindow.open(map, marker);
  });
}
}



//Place map on browser 
google.maps.event.addDomListener(window, 'load', initialize);






