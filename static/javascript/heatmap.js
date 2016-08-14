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


////////////
// marker //
////////////

// function addMarker() {
//   var myImageURL = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';
//   var image = myImageURL;
//   var nearSydney = new google.maps.LatLng(-34.788666, 150.41146)

// addMarker()


 ///////////////
 // basic map //
 ///////////////


////////////
// marker //
////////////

function addMarker() {
  var myImageURL = 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png';
  var image = myImageURL;
  var nearSydney = new google.maps.LatLng(-34.788666, 150.41146)
  var marker = new google.maps.Marker({
      position: nearSydney,
      map: map,
      title: 'Hover text',
      icon: image
  });
  return marker;
}

var marker = addMarker();

/////////////////
// info window //
/////////////////