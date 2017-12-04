# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Item
from login.models import User

# Create your tests here.
class MainTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_retrieveFoundItems(self):
        items = Item.objects.filter(status="Found")

        for item in items:
            self.assertEquals(item.status, 'Found')

    def test_retrieveLostItems(self):
        items = Item.objects.filter(status="Lost")

        for item in items:
            self.assertEquals(item.status, 'Lost')
    
    def test_postFoundItem(self):
        count = Item.objects.all().count()
        Item.objects.create(status="Found", name="Watch", description="a black watch", date="2015-05-23", latitude="200", longitude="15")
        count += 1
        self.assertEquals(Item.objects.all().count(), count)
    
    def test_createUser(self):
        count = User.objects.all().count()
        User.objects.create(email="test@django.com", zip_code="12345")
        count += 1
        self.assertEquals(User.objects.all().count(), count)
    
    def test_removeUser(self):
        User.objects.create(email="test@django.com", zip_code="12345")
        count = User.objects.all().count()
        a = User.objects.get(zip_code="12345")
        a.delete()
        count -= 1
        self.assertEquals(User.objects.all().count(), count)
