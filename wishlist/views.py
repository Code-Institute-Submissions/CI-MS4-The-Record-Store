from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
# Create your views here.

def view_wishlist(request):
    """ A view to show contents of the wishlist """
    return render(request, 'wishlist/view_wishlist.html')

def add_to_wishlist(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    
    
    if item_id in list(wishlist.keys()):
        messages.success(request, f'{product.name} already in your wishlist')
    else:
        wishlist[item_id] = 1
        messages.success(request, f'Added {product.name} to your wishlist')


    request.session['wishlist'] = wishlist
    return redirect(redirect_url)

def remove_from_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    wishlist = request.session.get('wishlist', {})
    wishlist.pop(item_id)
    request.session['wishlist'] = wishlist
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


