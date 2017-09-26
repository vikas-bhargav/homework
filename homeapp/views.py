from django.shortcuts import render, redirect

from random import choice
from .models import *
from homeapp.forms import CustumerForm, BookingForm
import datetime

# Create your views here.


def index(request):
    if request.method == 'POST':
        if 'save' in request.POST:

            customer_no = request.POST.get('phone_number')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            # set Customer
            customer_chk = Customer.objects.filter(phone_number=customer_no).exists()
            if customer_chk == False:
                customer_obj = Customer(first_name=first_name, last_name=first_name, phone_number=customer_no)
                customer_obj.save()
                message = 'Signup successfully.'
                form = BookingForm({'first_name': first_name, 'last_name': last_name, 'phone_number': customer_no})
            else:
                message = 'User alrady registered.'

                form = BookingForm({'first_name': first_name, 'last_name': last_name,
                                    'phone_number': customer_no})

            context = {'form': form, 'type': 'booking', 'message': message}
            return render(request, 'homeapp/index.html', context)

        if 'book' in request.POST:
            context = book(request)

            return render(request, 'homeapp/index.html', context)

    else:
        form = CustumerForm()
        context = {'form': form, 'type': 'signup'}

        return render(request, 'homeapp/index.html', context)


def book(request):
    customer_no = request.POST.get('phone_number')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    city = request.POST.get('city')
    get_date = request.POST.get('date')
    date = datetime.datetime.strptime(get_date, "%d-%m-%Y")

    customer_full_name = first_name + " " + last_name

    customer_obj = Customer.objects.get(phone_number=customer_no)
    city_obj = Cities.objects.get(id=city)
    cleaner_obj = Cleaner.objects.filter(cities=city_obj)

    book_summry = dict()
    cleaner_list = list()
    for cleaner in cleaner_obj:
        cleaner_chk = Booking.objects.filter(cleaner=cleaner).exists()
        if cleaner_chk == False:
            cleaner_list.append(cleaner)

    if len(cleaner_list) >= 1:
        cleaner_assign = choice(cleaner_list)
        book_obj = Booking(customer=customer_obj, cleaner=cleaner_assign, book_date=date, city_id=city)
        book_obj.save()

        # add bookoing detail in dictionary.
        book_summry['Customer Name'] = customer_full_name
        book_summry['City'] = city_obj.city_name
        book_summry['Booking Date'] = date
        book_summry['Cleaner'] = cleaner_assign.first_name + " " + cleaner_assign.last_name

        message = 'Book successfully!'
        context = {'type': 'booked', 'message': message, 'book_summry': book_summry}

        return context

    else:
        message = 'We could not fulfill your request at this time.'
        form = BookingForm({'first_name': first_name, 'last_name': last_name, 'phone_umber': customer_no})
        context = {'form': form, 'type': 'booking', 'message': message}

        return context
