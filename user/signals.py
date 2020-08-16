from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("signal called")
    if created:
        # Profile.objects.create(user=instance)
        profile = Profile(user=instance)
        profile.save()

post_save.connect(create_user_profile, sender=User)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print("signal called")
    instance.profile.save()

