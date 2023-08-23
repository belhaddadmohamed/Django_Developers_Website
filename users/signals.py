from django.db import models
from django.contrib.auth.models import User
from .models import Profile

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# This Signal will fire-up when the user is created (not updated !!!)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(user = user,
                               username = user.username,
                               email = user.email,
                               name = user.first_name)



# This Signal will fire-up when the user is updated 
def update_user(sender, instance, created, **kwargs):
    if created == False:
        profile = instance
        user = profile.user
        # Update the User
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()



# This Signal will fire-up when the profile is deleted (it will delete the User) !!! And to delete profile: we have (on_delete) in foreignKey!!!
def delete_user(sender, instance, **kwargs):
    user = instance.user    # Profile has a one to one relationship with 'User' model
    user.delete()



# Create Connections
post_save.connect(create_profile, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)


