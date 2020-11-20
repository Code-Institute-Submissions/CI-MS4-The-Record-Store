from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('addresses', views.addresses, name='addresses'),
    path('add_address', views.add_address, name='add_address'),
    path('edit_address/<item_id>', views.edit_address, name='edit_address'),
    path('delete_address/<item_id>', views.delete_address,
         name='delete_address'),
]
