from django import forms

from .models import *


class CustumerForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)

    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'type':
                                                                                           'number'}), required=True)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number']


class BookingForm(forms.ModelForm):
    first_name = forms.CharField(label='Customer Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)

    last_name = forms.CharField(label='Customer Name', widget=forms.TextInput(attrs={'class': 'form-control'}),
                                required=True)

    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'type': 'number'}),
                                   required=True)

    date = forms.DateTimeField()

    CITIES_CHOICES = set()
    city_obj = Cities.objects.all()
    for city in city_obj:
        CITIES_CHOICES.add((city.id, city.city_name))
    city = forms.MultipleChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                     choices=CITIES_CHOICES, label="Select City")

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'city', 'phone_number', 'date']
