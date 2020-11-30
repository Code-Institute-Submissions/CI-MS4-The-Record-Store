from django.db import models
from products.models import Product
from profiles.models import UserProfile

# Create your models here.


class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='wishlist')
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user_profile.user.username + "'s wishlist"