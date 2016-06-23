from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
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

# class LoginForm(AuthenticationForm):

# 	username = forms.CharField(max_length=254,
# 		widget=forms.TextInput(attrs={'autofocus': '', 'placeholder': 'Email'}),)
# 	password = forms.CharField(label="Password", strip=False,
# 		widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),)