import factory
import os
import contextlib
import random
import models


# Create factory for User model 
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        # similar to queryuser.models.User
        model = 'queryuser.User'
    
    first_name = "sen"
    last_name = "sundi"
    short_name = ""

    def __init__(self):
        """
        Construct a list of first names and last names present in the CSV files        
        """
        self.fnames = []
        # Get  first names file path
        fname_path = os.path.join(os.path.dirname(__file__), "first_names.csv")

        self.lnames = []
        # Get Last names file path
        lname_path = os.path.join(os.path.dirname(__file__), "last_names.csv")

        # Its good to use contextlib to close file handle as well as database 
        # sessions
        with contextlib.closing(open(fname_path,"r")) as ffile:
            self.fnames = ffile.read().split("\r")
        
        with contextlib.closing(open(lname_path,"r")) as lfile:
            self.lnames = lfile.read().split("\r")
        
        UserFactory.first_name = random.choice(self.fnames)
        UserFactory.last_name = random.choice(self.lnames)
        UserFactory.short_name = UserFactory.first_name[0]+UserFactory.last_name
        
        
    #def select_choice(self):
    #    """
    #    Get a random choice for first and last name and remove the choice made 
    #    to avoid duplications
    #    """
    #    first_name = random.choice(self.fnames)
    #    last_name = random.choice(self.lnames)
    #    self.fnames.remove(fchoice)
    #    self.lnames.remove(lchoice)
    
    #@select_choice
    #short_name = first_name[0]+last_name


# Create factory for UserLocation model 
class UserLocationFactory(factory.django.DjangoModelFactory):
	class Meta:
		# similar to queryuser.models.UserLocation
		model = 'queryuser.UserLocation'
