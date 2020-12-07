from django.db import models
from django.db.models import Sum
import uuid
from profiles.models import UserProfile
from products.models import Product
from django_countries.fields import CountryField


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    email = models.EmailField(
        max_length=254, null=False, blank=False, verbose_name="Email")
    first_name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="First Name")
    last_name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Last Name")
    address_line_1 = models.CharField(
        max_length=80, null=False, blank=False, verbose_name="Address Line 1")
    address_line_2 = models.CharField(
        max_length=80, null=False, blank=False, verbose_name="Address Line 2")
    town_or_city = models.CharField(
        max_length=80, null=False, blank=False, verbose_name="City/Town")
    county_or_province = models.CharField(max_length=80,
                                          null=False,
                                          blank=False,
                                          verbose_name="County/Province")
    country = CountryField(blank_label='Country *', null=False, blank=False)
    post_code_or_zip_code = models.CharField(
        max_length=80, null=False, blank=False, verbose_name="Postcode/Zip")
    phone_number = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="Phone")
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0,)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):

        self.order_total = self.line_items.aggregate(
            Sum('line_item_total'))['line_item_total__sum'] or 0

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='line_items')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    line_item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.line_item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
