$(document).ready(function() {

	$( "#search" ).autocomplete({
		minLength: 3,
		source: function (request, response) {
	        var matches = $.map(availableTags, function (school) {
	            if (school.toUpperCase().indexOf(request.term.toUpperCase()) === 0) {
	                return school;
	            }
	        });

	        response(matches.slice(0,10));
		}
	});

	$( "#search" ).keypress(function(event) {
		if (event.which==13){
			var query = $( "#search" ).val();
			goToSearchResults(query);
		}
	});
	$(".search-button").click(function() {
		var query = $( "#search" ).val();
		console.log(query)
		goToSearchResults(query);
	});

});

var availableTags = []

function goToSearchResults(searchQuery) {
	window.location.href = "listings/" + searchQuery;
}

// figure out how to convert from json
// also why it isn't reaching here?
function sendUniList(collegesList) {
	console.log("send listings")
	availableTags = collegesList;
}

