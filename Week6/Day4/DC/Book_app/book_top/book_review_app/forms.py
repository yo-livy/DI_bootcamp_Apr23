from django import forms
from .models import *

class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = '__all__'

from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', )