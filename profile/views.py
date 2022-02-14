from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from profile.models import Profile

class ProfileList(ListView):
    template_name = 'profile/profile_list.html'
    model = Profile
    context_object_name = 'profile'

class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'

class ProfileCreate(CreateView): # Is it working ???
    model = Profile
    fields = ['profile', 'doctor_title', 'image']
    template_name = 'profile/profile_new.html' # If not provided, searches for 'profile/profile_form.html'
    success_url = reverse_lazy('profile:profile_list')

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['profile', 'doctor_title', 'image']
    template_name = 'profile/profile_update.html'  # If not provided, searches for 'profile/profile_form.html'
    success_url = reverse_lazy('profile:profile_list')
