 
from django.test.utils import setup_test_environment
from django.test import TestCase

import contextlib
import os
import random

from queryuser.models import User, UserLocation
from factories import UserFactory, UserLocationFactory


setup_test_environment()

# TestCase class for model "User"
class UserTestcase(TestCase):

    def setUp(self):
        """
        This method will be initialized when a derived class of 
        TestCase is executed and used for specifying the pre-requisites
        """
        self.create_user_base()
        pass

    def create_user_base(self):
        """
        Create User base if does not exist already
        """
        if not User.objects.all():
            users = []
            # Iterate 20 times to create batch profiles of about 10000 users
            for iteration in range(20):

                # Create a batch of 500 users passing the short_name
                users.extend(UserFactory.create_batch(500))
				
				
    def test_add_user_if_no_data(self):
        """ 
        Check if the user table is empty, if yes, then insert data
        using data from first_names and last_names CSV files
        """
        self.assertNotEqual(User.objects.all(), [])
        
        
    def test_query_user(self):
        """
        Test to check if the user exists in table.
        NOTE - short_name field is used to query the database
        """
        defined_user = UserFactory.create(first_name="sen", last_name = "sundi", short_name="ssundi")
        defined_user.save()
        self.assertTrue(User.objects.get(short_name="ssundi") == defined_user)

    def tearDown(self):
        """
        This method is called as destructor when TestCase execution
        is complete and serves cleanup activities
        """
        pass

	
# TestCase class for model "UserLocation"
class UserLocationTestCase(TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	pass
