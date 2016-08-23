"use strict";

//Global markersArray
var markersArray = [];
var sliderDate = [];

var map = new google.maps.Map(document.getElementById('map-canvas'),{
    zoom: 2,
    minZoom: 2, 
    center: {lat: 45, lng: 10},
    // zoomControl: false,
    streetViewControl: false,
    scrollwheel: false
});

var infoWindow = new google.maps.InfoWindow({
    width: 150
});

function initialize() {
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
    }];

    var styledMapOptions = {
      name: 'Custom Style'
    };

    var customMapType = new google.maps.StyledMapType(
            styles,
            styledMapOptions);

    map.mapTypes.set('map_style', customMapType);
    map.setMapTypeId('map_style');
};

// Cet list of dates
function getArrayOfDates(){
    var arrayOfDates = [];
    $.get('/events', function (events){

        for (var key in events) {
            var one_event = events[key]

            arrayOfDates.push(parseInt(one_event.fullDate));
        }
    // Create the slider with the values from array date
    createSlider(arrayOfDates);
});
}


/* Add Slider */ 
function createSlider(sliderDate){
    $("#slider-1").slider({
        min: 0,
        max: sliderDate.length-1,
        
        // On slider slide, changes the values 
        slide: function(event, ui){
            // Want set values of the sliderDate array
            $('#slider-value').val(sliderDate[ui.value]);
            },

        // On slider change, parses and displays date, clears markers, and change markers   
        change: function (event, ui){
            //Store associated value to variable date and turn into string
            // console.log(ui.value);
            var date = sliderDate[ui.value].toString();

            // Separate into year, month, and day
            var year = date.substring(0,4)
            var month = date.substring(5,6)
            var day = date.substring(6,8)

            // console.log(year, month, day);

            // Pass parts into JavaScript Date method and convert resulting date object to string
            var date = new Date(year + '-' + month + '-' + day).toUTCString();
            
            // Just want the date without the GMT by string splicing
            date=date.split(' ').slice(0, 4).join(' ')

            // Show in html
            $('#slider-value').html(date);
            // Clears all the markers on the map
            clearMap(); 
            //calls changeMap everytime the slider is moved
            changeMap(sliderDate[ui.value]);
            }, 
    });
    // Set the initial value of the map to be the first date of sliderDate array
    $("#slider-1").slider({
        value: 0,
    })
};

// TODO : To clear the map 
function clearMap(){
    for (var i = 0; i < markersArray.length; i++){
        markersArray[i].setMap(null);
    }
    markersArray = [];
}

// Retrieving events information with AJAX
function changeMap(fullDate){

    $.get('/events/' + fullDate + '.json', function (events){
        var events, marker, html;

        for (var key in events) {
            var one_event = events[key]

            //Define markers
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(one_event.latitude, one_event.longitude),
                map: map,
                opacity: 0.7,
            });

            markersArray.push(marker);

            // Define markers in a circle
          //   marker = new google.maps.Circle ({
          //       strokeColor: '#FF0000',
          //       strokeOpacity: 0.8,
          //       strokeWeight: 2,
          //       fillColor: '#FF0000',
          //       fillOpacity: 0.35,
          //       map: map,
          //       center: new google.maps.LatLng(one_event.latitude, one_event.longitude),
          //       radius: 80000,
          //       // radius: Math.sqrt(citymap[city].population) * 100
          // });


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

//Place map on browser 
getArrayOfDates();

google.maps.event.addDomListener(window, 'load', initialize);