from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

ACCESS_LEVELS = [ ('o', 'owner'), ('u', 'user')]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS, null=True)

    def __str__(self):
        return str(self.user.username)
        
@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance)



class Operation_obj(models.Model):
    user = models.ForeignKey('auth.User')
    eq = models.CharField(max_length = 255)
    answer = models.IntegerField()
