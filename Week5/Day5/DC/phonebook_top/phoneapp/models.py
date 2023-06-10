from django.db import models
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()  
    address = models.CharField()

    def __str__(self):
        return self.name


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'formatted_phone_number')
    search_fields = ('phone_number', 'email', 'name')
    exclude = ('id',)

    def formatted_phone_number(self, obj):
        return obj.phone_number.as_international

    formatted_phone_number.short_description = 'Phone Number'
    formatted_phone_number.admin_order_field = 'phone_number'

    formfield_overrides = {
        PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget}
    }


