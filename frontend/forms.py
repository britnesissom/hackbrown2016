from django import forms

from .models import Listing, Review

class ListingForm(forms.ModelForm):

  class Meta:
    model = Listing
    fields = ('listing_name', 'school', 'address', 'price', 'rooms', 'bathrooms', 'comments')
    widgets = {'school': forms.HiddenInput(), 'comments': forms.Textarea(attrs={'rows':3, 'cols':20})}

class ReviewForm(forms.ModelForm):
    
  class Meta:
    model = Review
    fields = ('user', 'description', 'price', 'cleanliness', 'heating', 'appliances', 'bathrooms', 'rooms', 'll_avail', 'll_helpful', 'll_personality', 'comments', 'listing_id')
    widgets = {'listing_id': forms.HiddenInput(), 'comments': forms.Textarea(attrs={'rows':3, 'cols':20})}
