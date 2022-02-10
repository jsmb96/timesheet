from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from profiles.models import Profile

class ProfileList(ListView):
    template_name = 'profiles/profile_list.html'
    model = Profile
    context_object_name = 'profiles'

class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles/profiles_detail.html'

class ProfileCreate(CreateView):
    model = Profile
    fields = ['profile', 'doctor_title', 'image']
    template_name = 'profiles/profiles_new.html' # If not provided, searches for 'profiles/profiles_form.html'
    success_url = reverse_lazy('profiles:profiles_list')

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['profile', 'doctor_title', 'image']
    template_name = 'profiles/profiles_update.html'  # If not provided, searches for 'profiles/profiles_form.html'
    success_url = reverse_lazy('profiles:profiles_list')