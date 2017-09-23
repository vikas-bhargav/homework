from django.db import models
import datetime
# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name



class Cities(models.Model):
    CITIES_CHOICES = (
        ('mumbai', 'Mumbai'),
        ('ahmedabad', 'Ahmedabad'),
        ('indore', 'Indore'),
        ('pune', 'Pune'),
    )
    city_name = models.CharField(max_length=200, choices=CITIES_CHOICES)

    def __str__(self):
        return self.city_name


class Cleaner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    quality_score = models.FloatField(5)
    city = models.ForeignKey(Cities)
    def __str__(self):
        return self.first_name


class Booking1(models.Model):
    customer = models.ForeignKey(Customer)
    cleaner = models.ForeignKey(Cleaner)
    date = models.DateTimeField()


    def __str__(self):
        return self.customer
