from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from users.models import User

class UserList(ListView):
    template_name = 'users/user_list.html'
    model = User
    context_object_name = 'users'

