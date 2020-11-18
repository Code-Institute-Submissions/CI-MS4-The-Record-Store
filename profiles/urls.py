from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('addresses', views.addresses, name='addresses'),
]