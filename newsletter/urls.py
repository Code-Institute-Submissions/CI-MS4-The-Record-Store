from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up_to_newsletter, name='sign_up_to_newsletter')
]