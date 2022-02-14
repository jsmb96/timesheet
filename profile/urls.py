from django.urls import path

from profile import views

app_name = 'profile'

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile_list'),
    path('<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('new/', views.ProfileCreate.as_view(), name='profile_new'),
    path('<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
]