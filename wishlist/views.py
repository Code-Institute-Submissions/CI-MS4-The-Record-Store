from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Wishlist
from profiles.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist

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
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        users_wishlist = Wishlist.objects.get(user_profile=user_profile)
        users_wishlist.products.add(product)

    return redirect(redirect_url)


def remove_from_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    wishlist = request.session.get('wishlist', {})
    wishlist.pop(item_id)
    request.session['wishlist'] = wishlist
    redirect_url = request.POST.get('redirect_url')
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        users_wishlist = Wishlist.objects.get(user_profile=user_profile)
        users_wishlist.products.remove(product)

    return redirect(redirect_url)


def remove_all_from_wishlist(request):

    wishlist = request.session.get('wishlist', {})
    wishlist.clear()
    request.session['wishlist'] = wishlist
    redirect_url = request.POST.get('redirect_url')
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        users_wishlist = Wishlist.objects.get(user_profile=user_profile)
        users_wishlist.products.clear()
    return redirect(redirect_url)


def add_wishlist_to_cart(request):

    wishlist = request.session.get('wishlist', {})
    cart = request.session.get('cart', {})

    for wishlist_item in wishlist:
        cart[wishlist_item] = 1
    request.session['cart'] = cart
    messages.success(request, 'Added all wishlist items to your cart')
    redirect_url = request.POST.get('redirect_url')

    return redirect(redirect_url)


def update_wishlist(user, session):
    # check if there is a wishlist attached to the profile
    # if there is update the wishlist session/contexts
    # If there is no wishlist attached to the profile
    # then check if there is a wishlist in the session/contexts
    # attach it to the profile
    if user.is_authenticated:

        user_profile = UserProfile.objects.get(user=user)
        try:
            profile_wishlist = Wishlist.objects.get(user_profile=user_profile)
        except ObjectDoesNotExist:
            # If the user doesn't have a wishlist create one
            profile_wishlist = Wishlist()
            profile_wishlist.user_profile = user_profile
            profile_wishlist.save()

        # The profile doesn't have a saved wishlist
        if profile_wishlist is None:
            session_wishlist = session.get('wishlist')
            # If there is a session wishlist then create a 
            # profile wishlist and add the session wishlist to it
            if session_wishlist is not None:
                new_wishlist = Wishlist()
                new_wishlist.user_profile = user_profile
                new_wishlist.name = f"{user.username}'s wishlist"
                new_wishlist.save()
                for wishlist_item in session_wishlist:
                    new_wishlist.products.add(wishlist_item)
                new_wishlist.save()
        # The profile has a saved wishlist
        else:
            session_wishlist = session.get('wishlist', {})
            # If the session wishlist is empty then add the 
            # profile wishlist to it
            if session_wishlist is None:
                for wishlist_item in profile_wishlist.products.all():
                    if wishlist_item not in list(session_wishlist.keys()):
                        session_wishlist[wishlist_item.pk] = 1
            # A session wishlist and profile wishlist exists so merge them
            else:
                # Add any products in the session wishlist that aren't 
                # in the profile wishlist to the profile wishlist
                profile_wishlist_products = profile_wishlist.products.all()

                for wishlist_item in session_wishlist:
                    product_is_in_profile_wishlist = False
                    for product in profile_wishlist_products:
                        if wishlist_item == product.pk:
                            product_is_in_profile_wishlist = True
                    if product_is_in_profile_wishlist is False:
                        profile_wishlist.products.add(wishlist_item)
                        profile_wishlist.save()

                session_wishlist.clear()
                for wishlist_item in profile_wishlist.products.all():
                    session_wishlist[wishlist_item.pk] = 1

            session['wishlist'] = session_wishlist
