$(document).ready(function() {
	$(".replace").html("" + avgRating);
});

var avgRating;

function sendRating(rating) {
	avgRating = (rating.cleanliness + rating.heating + rating.appliances + rating.bathrooms + rating.rooms + rating.ll_avail + rating.ll_helpful + rating.ll_personality) / 8;
}