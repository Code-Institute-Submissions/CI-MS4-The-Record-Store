from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def add_product(request):
    """ Add a product to the store """

    template = 'products/add_product.html'
    context = {
    }

    return render(request, template, context)