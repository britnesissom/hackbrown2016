from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json

from .models import Listing, School, Review
from .forms import ListingForm, ReviewForm

schools = School.objects.all()

school_list = []
for school in schools:
	school_list.append(school.name)

# Create your views here.
def index(request):
	return render(request, 'frontend/index.html', {'schools': json.dumps(school_list)})

def db(request):
	listings = Listing.objects.all()
	return render(request, 'frontend/db.html', {'listings': listings})

def school_db(request):
	return render(request, 'frontend/db_school.html', {'schools': json.dumps(school_list)})

def display_listings(request, school):

	school_obj = School.objects.get(name=school)
	listings = Listing.objects.filter(school=school)

	return render(request, 'frontend/listings.html', {'school': school_obj, 'listings': listings, 'schools': json.dumps(school_list)})

def listing_reviews(request, pk):
	reviews = Review.objects.filter(listing_id=pk)
	return render(request, 'frontend/reviews.html', {'schools': json.dumps(school_list), 'reviews': reviews})

#@login_required
def submit_listing(request, school_id):

	school = get_object_or_404(School, id=school_id)

	if request.method == 'POST':
		form = ListingForm(request.POST)
		if form.is_valid():
			listing = form.save(commit=False)
			listing.author = request.user
			listing.school = school.name
			listing.address = request.address
			listing.price = request.price
			listing.rooms = request.rooms
			listing.bathrooms = request.bathrooms
			listing.comments = request.comments
			listing.save()
			return redirect('frontend.views.display_listings', pk=listing.pk)
	else:
		form = ListingForm(initial={'school': school})

	return render(request, 'frontend/listing_new.html', {'form': form, 'school': school, 'id': school_id, 'schools': json.dumps(school_list)})


def submit_review(request, pk):
	form = ReviewForm()
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.user = request.user
			review.description = request.description
			review.price = request.price
			review.cleanliness = request.cleanliness
			review.heating = request.heating
			review.appliances = request.appliances
			review.bathrooms = request.bathrooms
			review.rooms = request.rooms
			review.ll_avail = request.ll_avail
			review.ll_helpful = request.ll_helpful
			review.ll_personality = request.ll_personality
			review.comments = request.comments
			review.listing_id = request.listing_id
			review.save()
			return redirect('frontend.views.listing_reviews', pk=review.listing_id)
	else:
		form = ReviewForm(initial={'listing_id': pk})

	return render(request, 'frontend/reviews.html', {'form': form, 'listing_id': pk, 'schools': json.dumps(school_list)})
