from django.db import models
from django.contrib.auth.models import User
from films.models import Film

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    def __str__(self):
        return self.user.username

