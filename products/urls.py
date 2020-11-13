from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('add/', views.add_product, name='add_product'),
]