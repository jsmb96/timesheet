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
    location = models.CharField(default='',max_length=20)

    def _str_(self):
        return self.location

class Workday(models.Model):
    file_number = models.IntegerField(primary_key=True, default=1)
    profile = models.ForeignKey(Profile,null=True, on_delete = models.CASCADE) # profile connected to auth.user
    time_in = models.DateTimeField(default=date.today, null=True)
    time_out = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location,null=True, on_delete = models.CASCADE)
    sector = models.CharField(null=True,max_length = 20)
    # hours_code = models.CharField(max_length = 5)
    hours_code = forms.CharField(label='Hours Code', widget = forms.Select(choices=PAYROLL))
    FBP_payroll = models.CharField(default='$', max_length = 5)
    AMCO_payroll = models.CharField(default='$', max_length = 5)

    def get_absolute_url(self):  # reverve mapping url
        return reverse('workday:workday_detail', kwargs={'pkr': self.workday.pk, 'pk': self.pk})

    def _str_(self):
        return self.file_number,self.profile

