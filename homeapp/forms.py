from django import forms

from .models import *


class CustumerForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    phoneNumber = forms.CharField(max_length=10, widget=forms.NumberInput(
        attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phoneNumber']

class BookingForm(forms.ModelForm):
    first_name = forms.CharField(label='Customer Name',widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    last_name = forms.CharField(label='Customer Name',widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)
    phoneNumber = forms.CharField(max_length=10, widget=forms.NumberInput(
        attrs={'class': 'form-control'}), required=False)
    date = forms.DateTimeField()


    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'phoneNumber', 'date']

