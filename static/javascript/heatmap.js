"use strict";

function initialize() {
            var mapOptions = {
                center: new google.maps.LatLng(45, 10),
                zoom: 2,
                minZoom: 2, 
                center: {lat: 45, lng: 10}
            };

            var map = new google.maps.Map(
                    document.getElementById('map-canvas'),
                    mapOptions);

            var marker = new google.maps.Marker({
                map: map,
                place: {
                    location: {lat: 42.58, lng: 21},
                    query: 'Kosovo'
                }
            });

            // Construct a new InfoWindow.
            var infowindow = new google.maps.InfoWindow({
                content: 'Kosovo'
            });

            // Opens the InfoWindow when marker is clicked.
            marker.addListener('click', function () {
                infowindow.open(map, marker);
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

            }

        google.maps.event.addDomListener(window, 'load', initialize);
