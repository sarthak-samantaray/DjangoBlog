from  django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



# When  a User is saved send this post_save signal.
# And this signal will be received by the receiver
# Receiver is the create_profile function,
#  if a user is created then make a profile using that instance
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created :
        Profile.objects.create(user=instance)


# save_post 

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()