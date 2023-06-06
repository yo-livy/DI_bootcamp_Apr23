from django import forms
from .models import *

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RatingChoices.choices, widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = '__all__'
