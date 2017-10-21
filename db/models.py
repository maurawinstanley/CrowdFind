from django.db import models

class User(models.Model):
    email = models.EmailField()
    zip_code = models.TextField()

class Item(models.Model):
    user = models.ForeignKey(User)
    name = models.TextField()
    descirption = models.TextField()
    location = models.TextField()
