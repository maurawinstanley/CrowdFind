from django.db import models

class User(models.Model):
    email = models.EmailField()
    zip_code = models.IntegerField()