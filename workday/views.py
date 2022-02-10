from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, ListView

from workday.forms import WorkdayForm
from workday.models import Workday,Location,PAYROLL

class WorkdayList(ListView):
    template_name = 'workday/workday_list.html'
    model = Workday
    context_object_name = 'workday'

class WorkdayDetail(DetailView): #object === workday
    model = Workday
    template_name = 'workday/workday_detail.html'
    extra_context = {'PAYROLL': PAYROLL}

class LocationDetail(DetailView): #object === workday
    model = Location
    template_name = 'location/location_detail.html'


class WorkdayCreate(LoginRequiredMixin, CreateView):
    model = Workday
    form_class = WorkdayForm
    template_name = 'workday/workday_create.html'
    success_url = reverse_lazy('workday:workday_list')
    login_url = 'login'# appname:viewname accounts/login

    def form_valid(self, form): #MRO
        form.instance.user = self.request.user # logged in user
        return super(WorkdayCreate, self).form_valid(form)
    #
    # def get(self):
    #     pass
    # def post(self):
    #     pass