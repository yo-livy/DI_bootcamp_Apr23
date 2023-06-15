from django import forms
from .models import *
from django.forms import formset_factory 

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


class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = '__all__'

ProducerFormSet = forms.modelformset_factory(Producer, form=ProducerForm)
