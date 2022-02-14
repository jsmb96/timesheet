from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView


# def Home():
#

from django.shortcuts import render

def home(request):
   return render(request, 'home.html')