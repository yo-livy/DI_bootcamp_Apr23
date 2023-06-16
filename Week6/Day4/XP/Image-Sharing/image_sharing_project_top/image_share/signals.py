from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Image, Profile
from django.contrib.auth.models import User


@receiver(post_save, sender=Image)
def update_profile(sender, instance, created, **kwargs):
    if created:
        instance.user.profile.total_images = Image.objects.filter(user=instance.user).count()
        instance.user.profile.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
