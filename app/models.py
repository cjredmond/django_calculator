from django.db import models

ACCESS_LEVELS = [ ('o', 'owner'), ('u', 'user')]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

class Operation(models.Model):
    user = models.ForeignKey('auth.User')
    eq = models.CharField(max_length = 255)
