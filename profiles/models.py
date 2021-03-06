from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField
# Create your models here.


class Address(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    address_line_1 = models.CharField(max_length=254)
    address_line_2 = models.CharField(max_length=254)
    town_or_city = models.CharField(max_length=254)
    county_or_province = models.CharField(max_length=254)
    country = CountryField(blank_label='Country *',
                           null=False, blank=False, max_length=256)
    post_code_or_zip_code = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    primary_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address_line_1


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_address = models.ForeignKey(
        Address, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
