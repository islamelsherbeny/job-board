# this file i made to make a profile for each user not using the admin page  8 26:00

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#this is confusing but it's hpe it is done in django
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()