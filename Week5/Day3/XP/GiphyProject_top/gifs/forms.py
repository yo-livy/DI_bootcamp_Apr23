from django import forms
from .models import Category, Gif

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class GifForm(forms.ModelForm):
    category_field = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Gif
        fields = '__all__'
