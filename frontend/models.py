from django.db import models
from django.utils import timezone

# Create your models here.
class Listing(models.Model):
   author = models.ForeignKey('auth.User')
   listing_name = models.CharField(max_length=200)
   school = models.CharField(max_length=100, default="school")
   address = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=7, decimal_places=2)
   rooms = models.SmallIntegerField()
   bathrooms = models.SmallIntegerField()
   comments = models.TextField(blank=True, default="N/A")
   created_date = models.DateTimeField(default=timezone.now)

   def publish(self):
      self.created_date = timezone.now()
      self.save()

   def __str__(self):
      return self.listing_name

class Review(models.Model):
   user = models.CharField(max_length=100)
   description = models.TextField()
   price = models.DecimalField(max_digits=7, decimal_places=2)
   cleanliness = models.SmallIntegerField()
   heating = models.SmallIntegerField()
   appliances = models.SmallIntegerField()
   bathrooms = models.SmallIntegerField()
   rooms = models.SmallIntegerField()
   ll_avail = models.SmallIntegerField()
   ll_helpful = models.SmallIntegerField()
   ll_personality = models.SmallIntegerField()
   comments = models.TextField(blank=True, default="N/A")
   listing_id = models.IntegerField() 
   created_date = models.DateTimeField(default=timezone.now)

   def publish(self):
      self.created_date = timezone.now()
      self.save()

   def __str__(self):
      return self.listing_id

class School(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name
