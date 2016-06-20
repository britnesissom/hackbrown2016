$(document).ready(function() {
	$( ".listing" ).click(function() {
		var list_id = $(this).find(".id_align").val();
		alert(list_id);
		var location = "/create_review/" + list_id;
		alert('' + location);
		window.location.href = location;
	});

	$( ".create_listing" ).click(function() {
		window.location.href = "/listings/" + id + "/new/";
	});

	/* if no listings, how do we pick listing_id to send? should we just do school name instead? 
	no because this is a listing for a specific place 
	so how to make review for listing that doesn't exist yet? */

});

var id;

function sendSchool(schoolId) {
	id = schoolId;
}


var map;
var geocoder;
var addresses = ["49 Preston St, Providence","245 Waterman St, Providence"];

function initMap() {
	setupMapElement();
	//makeGeocoder();
	//makeMarkers();
}


function setupMapElement() { 
	var myLatLng = {lat: 41.8236, lng: -71.4222};
	  /*here we may be able to put in instead: (but not sure if just the school name
	  	 //is enough of an address)
	  geocoder.geocode({'address': school}, function(results, status) {
	    if (status === google.maps.GeocoderStatus.OK) {
	      	myLatLng = results[0].geometry.school;
	      	} else {
		  	alert('Geocode was not successful for the following reason: ' + status);
		  	myLatLng = {lat: 41.8236, lng: -71.4222}; //Providence coordinates
		}
	});*/

	map = new google.maps.Map(document.getElementById('map'), {
		center: myLatLng,
		zoom: 14
	});
}

function makeMarkers() {
	for (i = 0; i < addresses.length; i++) { 
		addMarkerForAddress(addresses[i]);
	}
}

function makeGeocoder() {
	geocoder = new google.maps.Geocoder();
}


function addMarkerForAddress(address) {
	geocoder.geocode({'address': address}, function(results, status) {
		if (status === google.maps.GeocoderStatus.OK) {
			result = results[0].geometry.school;

			var marker = new google.maps.Marker({
				position: result,
				map: map,
			    title: address //
			}); 
		} else {
			alert('Geocode was not successful for the following reason: ' + status);
		}
	});
}