from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):

    wishlist_items = []
    wishlist = request.session.get('wishlist', {})
    context = {
        'wishlist_items': wishlist_items,
    }
    
    return context
