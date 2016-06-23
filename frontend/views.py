from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json

from .models import Listing, School, Review
from .forms import ListingForm, ReviewForm

def get_schools():
	schools = School.objects.all()

	school_list = []
	for school in schools:
		school_list.append(school.name)

	return school_list

# Create your views here.
def index(request):
	return render(request, 'frontend/index.html', {'schools': json.dumps(get_schools())})

def db(request):
	listings = Listing.objects.all()
	return render(request, 'frontend/db.html', {'listings': listings})

def school_db(request):
	return render(request, 'frontend/db_school.html', {'schools': json.dumps(get_schools())})

def display_listings(request, school):

	school_obj = School.objects.get(name=school)
	print(school_obj)
	listings = Listing.objects.filter(school=school)

	return render(request, 'frontend/listings.html', {'school': school_obj, 'listings': listings, 'schools': json.dumps(get_schools())})

def listing_reviews(request, pk):
	reviews = Review.objects.filter(listing_id=pk)
	return render(request, 'frontend/reviews.html', {'schools': json.dumps(get_schools()), 'reviews': reviews})

#@login_required
def submit_listing(request, pk):

	school = get_object_or_404(School, id=pk)

	if request.method == 'POST':
		form = ListingForm(request.POST)

		if form.is_valid():
			listing = form.save(commit=False)
			listing.author = request.user
			listing.published_date = timezone.now()
			listing.save()
			return redirect(reverse('display_listings', kwargs={'school': school.name}))
		else:
			print(form.errors)
	else:
		form = ListingForm(initial={'school': school})

	return render(request, 'frontend/listing_new.html', {'form': form, 'school': school, 'id': pk, 'schools': json.dumps(get_schools())})


def submit_review(request, pk):
	form = ReviewForm()
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.published_date = timezone.now()
			review.save()
			return redirect(reverse('listing_reviews', kwargs={'pk': review.listing_id}))
	else:
		form = ReviewForm(initial={'listing_id': pk})

	return render(request, 'frontend/reviews.html', {'form': form, 'listing_id': pk, 'schools': json.dumps(get_schools())})
