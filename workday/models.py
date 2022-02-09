from datetime import date
from django.db import models
from django.urls import reverse
from django import forms
from profiles.models import Profile

# Create your models here.
from django.utils import timezone

PAYROLL= [
    ('fbp', 'FBP'),
    ('amco', 'AMCO'),]

class Location(models.Model):
    Location = models.CharField(max_length=20)

class Workday(models.Model):
    file_number = models.IntegerField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) # profile connected to auth.user
    time_in = models.DateTimeField(default=date.today, null=True)
    time_out = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sector = models.CharField(max_length = 20)
    # hours_code = models.CharField(max_length = 5)
    hours_code = forms.CharField(label='Hours Code', widget=forms.Select(choices=PAYROLL))
    FBP_payroll = models.CharField(default='$', max_length = 5) # Now you have the HoursCode, you don't need these 2 parameters 
    AMCO_payroll = models.CharField(default='$', max_length = 5)

    def get_absolute_url (self) :
        return reverse('workday:workday_list')

    def _str_(self):
        return self.location

