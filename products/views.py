from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Product, Artist, Label, Genre, Format, Colour, Tag

# Create your views here.


@login_required
def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        add_dynamically_created_data_to_the_database(form)
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


def add_dynamically_created_data_to_the_database(form):
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

    genre_submitted_in_the_form = form.data['genre']
    if(not genre_submitted_in_the_form.isnumeric()):
        # Create a new label and insert it into the database
        new_genre_name = genre_submitted_in_the_form.lower()
        new_genre_name = new_genre_name.replace(" ", "_")
        new_genre_friendly_name = genre_submitted_in_the_form
        new_genre = Genre()
        new_genre.name = new_genre_name
        new_genre.friendly_name = new_genre_friendly_name
        new_genre.save()
    
    format_submitted_in_the_form = form.data['format']
    if(not format_submitted_in_the_form.isnumeric()):
        # Create a new label and insert it into the database
        new_format_name = format_submitted_in_the_form.lower()
        new_format_name = new_format_name.replace(" ", "_")
        new_format_friendly_name = format_submitted_in_the_form
        new_format = Format()
        new_format.name = new_format_name
        new_format.friendly_name = new_format_friendly_name
        new_format.save()

    colour_submitted_in_the_form = form.data['label']
    if(not colour_submitted_in_the_form.isnumeric()):
        # Create a new label and insert it into the database
        new_colour_name = colour_submitted_in_the_form.lower()
        new_colour_name = new_colour_name.replace(" ", "_")
        new_colour_friendly_name = colour_submitted_in_the_form
        new_colour = Colour()
        new_colour.name = new_colour_name
        new_colour.friendly_name = new_colour_friendly_name
        new_colour.save()