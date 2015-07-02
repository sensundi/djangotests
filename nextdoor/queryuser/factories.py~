import factory

from queryuser import models
from django.test.utils import setup_test_environment

# Create factory for UserLocation model 
class UserLocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        # similar to queryuser.models.UserLocation
        model = 'queryuser.UserLocation'
    
    lat = 0.0
    lng = 0.0
    user = None

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        obj = model_class(*args, **kwargs)
        obj.user = kwargs["user"]
        obj.save()
        return obj


# Create factory for User model 
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        # similar to queryuser.models.User
        model = 'queryuser.User'
    
    first_name = "sen"
    last_name = "sundi"
    short_name = ""
    #location = factory.RelatedFactory(UserLocationFactory, 'user')

    



