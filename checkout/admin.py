from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_item_total',)


# Register your models here.
class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'first_name',
              'last_name', 'email', 'phone_number', 'country',
              'post_code_or_zip_code', 'town_or_city', 'address_line_1',
              'address_line_2', 'county_or_province', 'delivery_cost',
              'order_total', 'grand_total')

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'stripe_pid')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
