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
        // Set initial value to 197 (index for July 16th) which is the day after the Turkish Coup
        value: 197,
    })
};

// To clear markers on map 
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
        var locations = {};

        for (var key in events) {
            var one_event = events[key]

            var latitude = parseInt(one_event.latitude);
            var longitude = parseInt(one_event.longitude);
            var count = 1; // count of number of latlng
            var url = one_event.url;

            var latlng = [latitude, longitude];

            if (latlng in locations) {
                // locations[latlng] = {'count': 0,'url':'None'};
                locations[latlng]['count'] = locations[latlng]['count'] + 1;
                if (!(url in locations[latlng]['url'])){
                    locations[latlng]['url'].push(url);
                };
            } else {
                locations[latlng] = {'count': 0,'url':[]};
                locations[latlng]['count'] = 1;
                locations[latlng]['url'].push(url);
            };
            }

        // Loop through each location to place markers 

        for (var latlng in locations) {
            latlng = latlng.split(',');
    
        // Define markers in a circle
        marker = new google.maps.Circle ({
            strokeColor: '#FFFFFF',
            strokeOpacity: 0.8,
            strokeWeight: 1,
            fillColor: '#FF0000',
            fillOpacity: 0.2,
            map: map,
            center: new google.maps.LatLng(latlng[0], latlng[1]),
            position: new google.maps.LatLng(latlng[0], latlng[1]),
            radius: locations[latlng]['count'] * 11000,
        });

        markersArray.push(marker);

        var arrayOfURLs = (locations[latlng]['url'])

        html = (
            '<div class="window-content">' +
                '<a target="_blank" href='+ arrayOfURLs[0] + '>' + arrayOfURLs[0] + '</a>' +
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
