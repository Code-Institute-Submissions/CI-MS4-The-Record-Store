from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Product, Artist, Label

# Create your views here.


@login_required
def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        add_dynamically_created_data_to_the_database()
        if form.is_valid():

            print("Form is valid")
            print(form.cleaned_data['artist'])
            # Generate SKU
            # sku = str(form.cleaned_data['name'])[0:3]+"/"+str(form.cleaned_data['artist'])[0:3]+"/"+str(form.cleaned_data['label'])[0:3]+"/"+str(form.cleaned_data['colour'])[0:3]+"/"+str(form.cleaned_data['format'])[0:3]
            # sku = sku.upper()

            # product = form.save()
            # product.sku = sku
            # product.save()
            return redirect(reverse('home'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_dynamically_created_data_to_the_database():
    # Check if there is an Artist not in the database
    artist_submitted_in_the_form = form.data['artist']
    if(not artist_submitted_in_the_form.isnumeric()):
        # Create a new artist and insert it into the database
        new_artist_name = artist_submitted_in_the_form.lower()
        new_artist_name = new_artist_name.replace(" ", "_")
        new_artist_friendly_name = artist_submitted_in_the_form
        new_artist = Artist()
        new_artist.name = new_artist_name
        new_artist.friendly_name = new_artist_friendly_name
        new_artist.save()

    label_submitted_in_the_form = form.data['label']
    if(not label_submitted_in_the_form.isnumeric()):
        # Create a new label and insert it into the database
        new_label_name = label_submitted_in_the_form.lower()
        new_label_name = new_label_name.replace(" ", "_")
        new_label_friendly_name = label_submitted_in_the_form
        new_label = Label()
        new_label.name = new_label_name
        new_label.friendly_name = new_label_friendly_name
        new_label.save()
