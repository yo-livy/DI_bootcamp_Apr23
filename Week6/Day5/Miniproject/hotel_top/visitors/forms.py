from django import forms
from .models import Booking, ContactMessage
from django.forms.widgets import DateInput
from django.utils import timezone


class BookingForm(forms.ModelForm):
    check_in_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['room', 'check_in_date', 'check_out_date']
        widgets = {
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.initial['user'] = user  # Set initial value for 'user' field

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

        if check_in_date and check_out_date:
            today = timezone.now().date()
            if check_in_date < today:
                self.add_error('check_in_date', 'Check-in date cannot be in the past.')
            if check_out_date <= check_in_date:
                self.add_error('check_out_date', 'Check-out date must be after the check-in date.')
            if check_out_date == check_in_date:
                self.add_error('check_out_date', 'Minimum 1 night stay is required.')

        return cleaned_data
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
