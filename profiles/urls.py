from django.urls import path

from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile_list'),
]