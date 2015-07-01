from django.contrib.gis.db import models

# Create your models here.

class User(models.Model):
	# Define the fields of User table
	short_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	
	
class UserLocation(models.Model):
	# Define the fields of UserLocation table
	user = models.ForeignKey(User)
	area = models.IntegerField()
	lon = models.FloatField()
	lat = models.FloatField()

	# Add the user's location
	def add_user_location(user, lat, lng):
		pass

	# Get User location
	def get_user_location(user):
		pass

	# Get nearest user location for a given user
	def get_nearby_users(user, limit=140):
		pass
