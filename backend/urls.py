"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import django.contrib.auth.views

from django.contrib import admin
admin.autodiscover()

import frontend.views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^db', frontend.views.school_db, name='db'),
  url(r'^$', frontend.views.index, name='index'),
  url(r'^login/$', django.contrib.auth.views.login, name='login'),
  url(r'^logout/$', django.contrib.auth.views.logout, name='logout'),
  url(r'^listings/(?P<school>[\w\ \(\)]+)/?$', frontend.views.display_listings, name='display_listings'),
  url(r'^listings/(?P<pk>\d+)/new/$', frontend.views.submit_listing, name='submit_listing'),
  url(r'^reviews/(?P<pk>\d+)/?$', frontend.views.listing_reviews, name='listing_reviews'),
  url(r'^reviews/(?P<pk>\d+)/new/$', frontend.views.submit_review, name='submit_review'),
  url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
]
