from django.db import models
from django.contrib.auth.models import User
from .models import Profile

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# This Signal will fire-up when the user is created (not updated !!!)
def create_profile(sender, instance, created, **kwargs):
    print("Profile is created")
    if created:
        user = instance
        Profile.objects.create(user = user,
                               username = user.username,
                               email = user.email,
                               name = user.first_name)

post_save.connect(create_profile, sender=User)


# This Signal will fire-up when the profile is deleted (it will delete the User) !!! The reverse we have (on_delte) in foreignKey!!!
def delete_user(sender, instance, **kwargs):
    print("User is deleted")
    user = instance.user
    user.delete()

post_delete.connect(delete_user, sender=Profile)


