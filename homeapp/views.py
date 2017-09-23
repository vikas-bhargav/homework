from django.shortcuts import render

from .models import *
from homeapp.forms import CustumerForm, BookingForm

# Create your views here.

def index(request):
    if request.method == 'POST':

        customer_no = request.POST.get('phoneNumber')
        print("customer_no: ", customer_no)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # customer_full_name = request.POST.get('first_name') + " " + request.POST.get('last_name')
        customer_obj = Customer.objects.filter(phone_number=customer_no)
        print("customer_obj: ", len(customer_obj))
        if len(customer_obj) == 0:
            customer_obj = Customer(first_name=first_name, last_name=first_name, phone_number=customer_no)
            customer_obj.save()
            message = 'Signup successfully!'
        else:
            message = 'User alrady exist....!'

        form = BookingForm({'first_name': first_name, 'last_name': last_name, 'phoneNumber': customer_no})
        cities = Cities.objects.all()
        for c in cities:
            print(c.city_name, ": ", c.id)

        context = {'form': form, 'type': 'booking', 'message': message, 'cities': cities}

    else:
        print("final else----------------------")
        form = CustumerForm()
        context = {'form': form, 'type': 'signup'}

    return render(request, 'homeapp/index.html', context)

def book(request):

    if request.method == 'POST':

        customer_no = request.POST.get('phoneNumber')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_full_name = first_name + " " + last_name

        if len(customer_obj) == 0:
            customer_obj = Customer(first_name=first_name, last_name=first_name, phone_number=customer_no)
            customer_obj.save()
            message = 'Signup successfully!'
        else:
            message = 'User alrady exist....!'

        form = BookingForm({'first_name': first_name, 'last_name': last_name, 'phoneNumber': customer_no})
        context = {'form': form, 'type': 'booking', 'message': message}

    else:
        form = BookingForm()
        context = {'form': form, 'type': 'booking '}

    return render(request, 'homeapp/index.html', context)