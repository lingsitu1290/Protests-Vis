// var map, heatmap;

// function initMap() {
//   map = new google.maps.Map(document.getElementById('map'), {
//     zoom: 2,
//     minZoom: 2,
//     center: {lat: 45, lng: 10},
//     // mapTypeId: 'satellite'
//   });

//   heatmap = new google.maps.visualization.HeatmapLayer({
//     data: getPoints(),
//     map: map
//   });
// }

// function toggleHeatmap() {
//   heatmap.setMap(heatmap.getMap() ? null : map);
// }

// function changeGradient() {
//   var gradient = [
//     'rgba(0, 255, 255, 0)',
//     'rgba(0, 255, 255, 1)',
//     'rgba(0, 191, 255, 1)',
//     'rgba(0, 127, 255, 1)',
//     'rgba(0, 63, 255, 1)',
//     'rgba(0, 0, 255, 1)',
//     'rgba(0, 0, 223, 1)',
//     'rgba(0, 0, 191, 1)',
//     'rgba(0, 0, 159, 1)',
//     'rgba(0, 0, 127, 1)',
//     'rgba(63, 0, 91, 1)',
//     'rgba(127, 0, 63, 1)',
//     'rgba(191, 0, 31, 1)',
//     'rgba(255, 0, 0, 1)'
//   ]
//   heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
// }

// function changeRadius() {
//   heatmap.set('radius', heatmap.get('radius') ? null : 20);
// }

// function changeOpacity() {
//   heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
// }


// // Heatmap data: 500 Points
// function getPoints(results) {
//   var list_of_latlng = results
//   console.log(results);
//   // for (i=0; i<results.length; i++){
//   return [
//     new google.maps.LatLng(45, 10),
//   ];
// // }
// }

// //Grab lat/long data from server using AJAX
// function getData(){
//   $.get('/latlng', getPoints);
//   console.log("result");
// }

// getData();



"use strict";

function initialize() {
            // var mapOptions = {
            //     zoom: 2,
            //     minZoom: 2, 
            //     center: {lat: 45, lng: 10}
            // };

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


 // Retrieving the information with AJAX
$.get('/events/20160715.json', function (events) {
var events, marker, html;

for (var key in events) {
    var one_event = events[key]

      // Define the marker
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(parseInt(one_event.latitude), parseInt(one_event.longitude)),
        map: map
    });

    // Define the content of the infoWindow
    html = (
        '<div class="window-content">' +
            '<p>' + one_event.url + '</p>' +
        '</div>');

    // Inside the loop we call bindInfoWindow passing it the marker,
    // map, infoWindow and contentString
    bindInfoWindow(marker, map, infoWindow, html);
}

});

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



google.maps.event.addDomListener(window, 'load', initialize);


