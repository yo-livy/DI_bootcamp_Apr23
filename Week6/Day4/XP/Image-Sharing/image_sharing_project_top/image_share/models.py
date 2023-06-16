from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    total_images = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username



    

