from django.urls import re_path
from django.utils import timezone
from django.views.generic import View, ListView, UpdateView, DetailView

from workday import views
from workday.forms import WorkdayForm
from workday.models import Workday, Location
from workday.views import WorkdayDetail, WorkdayCreate, LocationDetail

app_name = 'workday'
urlpatterns = [
    # List latest 5 workdays, ex.: /workdays/
    re_path(r'^$',
            ListView.as_view(
                # model = workday,
                queryset=Workday.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
                context_object_name='latest_workday_list',
                template_name=' workday/workday_list.html'),
            name='workday_list'),

    # workday details, ex.: /workdays/1/
    re_path(r'^(?P<pk>\d+)/$',
            WorkdayDetail.as_view(),
            name='workday_detail'),

    # Create a workday, ex.: /workdays/create/
    re_path(r'^create/$',
            WorkdayCreate.as_view(),
            name='workday_create'),

    # # Update workday details, ex.: /workdays/1/update/
    # re_path(r'^(?P<pk>\d+)/update/$',
    #         UpdateView.as_view(
    #             model=workday,
    #             template_name='workday/workday_update.html',
    #             form_class=WorkdayForm),
    #         name='workday_update'),

    # workday location details, ex: /workdays/1/locations/1/
    re_path(r'^workdays/(?P<pkr>\d+)/locations/(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Location,
                template_name='workday/location_detail.html'),
            name='location_detail'),

    # # Create a workday location, ex.: /workdays/1/locations/create/
    # re_path(r'^workdays/(?P<pk>\d+)/locationes/create/$',
    #         locationCreate.as_view(),
    #         name='location_create'),

    # Update workday location details, ex.: /workdays/1/locations/1/edit/
    re_path(r'^workdays/(?P<pkr>\d+)/locations/(?P<pk>\d+)/edit/$',
            UpdateView.as_view(
                model=location,
                template_name='workday/workday_update.html',
                form_class=locationForm),
            name='location_update'),

    # Create a workday review, ex.: /workdays/1/reviews/create/
    re_path(r'^workdays/(?P<pk>\d+)/reviews/create/$',
            views.review_create,
            name='review_create'),
]
