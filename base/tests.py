from django.test import TestCase
from .models import Neighborhood, User, Post, Business
# Create your tests here.


from django.test import TestCase
from .models import Profile , Post, Comment 
from django.contrib.auth.models import User
# Create your tests here.

class NeighborhoodTestClass(TestCase):

    def setUp(self):
        self.user = User(id=1, user='alex')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()




   
    
