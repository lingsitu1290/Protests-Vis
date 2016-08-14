"use strict";

function initialize() {
          var mapOptions = {
             center: new google.maps.LatLng(45, 10),
             zoom: 2,
             minZoom: 2
          };
          var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
       }

       google.maps.event.addDomListener(window, 'load', initialize);