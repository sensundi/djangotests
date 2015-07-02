import math

from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.contrib.gis.geos import Point
from django.db.backends.signals import connection_created
from django.dispatch import receiver


# Create your models here.
class LocationManager(models.Manager):
    def nearby(self, latitude, longitude, proximity):
        """
        Return all object which distance to specified coordinates
        is less than proximity given in kilometers
        """
        # Great circle distance formula
        gcd = """
                6371 * acos(
                            cos(radians(%s)) * cos(radians(lat))
                            * cos(radians(lng) - radians(%s)) +
                            sin(radians(%s)) * sin(radians(lat))
                            )
                """
        gcd_lt = "{} < %s".format(gcd)
        return self.get_queryset()\
                        .exclude(lat=None)\
                        .exclude(lng=None)\
                        .extra(
                            select={'distance': gcd},
                            select_params=[latitude, longitude, latitude],
                            where=[gcd_lt],
                            params=[latitude, longitude, latitude, proximity],
                            order_by=['distance']
                   )


class User(models.Model):
    # Define the fields of User table
    short_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
	
	
class UserLocation(models.Model):
    # Define the fields of UserLocation table
    user = models.ForeignKey(User)
    lng = models.FloatField()
    lat = models.FloatField()
    location = models.PointField(blank=True, null=True)

    objects = LocationManager()

    # Override save method to create the location field
    # and save the object
    def save(self, *args, **kwargs):
        self.location = Point(self.lng, self.lat)
        super(UserLocation, self).save(*args, **kwargs)

@receiver(connection_created)
def extend_sqlite(connection=None, **kwargs):
    if connection.vendor == "sqlite":
        # sqlite doesn't natively support math functions, so add them
        cf = connection.connection.create_function
        cf('acos', 1, math.acos)
        cf('cos', 1, math.cos)
        cf('radians', 1, math.radians)
        cf('sin', 1, math.sin)

