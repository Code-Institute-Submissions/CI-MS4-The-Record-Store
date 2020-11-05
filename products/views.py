from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Product

# Create your views here.


@login_required
def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Generate SKU
            sku = str(form.cleaned_data['name'])[0:3]+"/"+str(form.cleaned_data['artist'])[0:3]+"/"+str(form.cleaned_data['label'])[0:3]+"/"+str(form.cleaned_data['colour'])[0:3]+"/"+str(form.cleaned_data['format'])[0:3]
            sku = sku.upper()
            
            product = form.save()
            product.sku = sku
            product.save()
            return redirect(reverse('add_product'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
