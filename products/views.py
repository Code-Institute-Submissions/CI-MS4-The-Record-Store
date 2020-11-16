from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Product, Artist, Label, Genre, Format, Colour, Tag

# Create your views here.


@login_required
def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        updated_request = request.POST.copy()
        updated_request = add_dynamically_created_data_to_the_database(updated_request)
        form = ProductForm(updated_request, request.FILES)
        if form.is_valid():
            # Generate SKU
            sku = str(form.cleaned_data['name'])[0:3]+"/"+str(form.cleaned_data['artist'])[0:3]+"/"+str(form.cleaned_data['label'])[0:3]+"/"+str(form.cleaned_data['colour'])[0:3]+"/"+str(form.cleaned_data['format'])[0:3]
            sku = sku.upper()

            product = form.save()
            product.sku = sku
            product.save()
            return redirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def add_dynamically_created_data_to_the_database(updated_request):
    # Check if there is an Artist not in the database
    artist_submitted_in_the_form = updated_request['artist']
    if(not artist_submitted_in_the_form.isnumeric()):
        # Create a new artist and insert it into the database
        new_artist_name = artist_submitted_in_the_form.lower()
        new_artist_name = new_artist_name.replace(" ", "_")
        new_artist_friendly_name = artist_submitted_in_the_form
        new_artist = Artist()
        new_artist.name = new_artist_name
        new_artist.friendly_name = new_artist_friendly_name
        new_artist.save()
        updated_request.update({'artist': Artist.objects.get(name = new_artist.name).pk})


    label_submitted_in_the_form = updated_request['label']
    if(not label_submitted_in_the_form.isnumeric()):
        # Create a new label and insert it into the database
        new_label_name = label_submitted_in_the_form.lower()
        new_label_name = new_label_name.replace(" ", "_")
        new_label_friendly_name = label_submitted_in_the_form
        new_label = Label()
        new_label.name = new_label_name
        new_label.friendly_name = new_label_friendly_name
        new_label.save()
        updated_request.update({'label': Label.objects.get(name = new_label.name).pk})

    genre_submitted_in_the_form = updated_request['genre']
    if(not genre_submitted_in_the_form.isnumeric()):
        # Create a new label and insert it into the database
        new_genre_name = genre_submitted_in_the_form.lower()
        new_genre_name = new_genre_name.replace(" ", "_")
        new_genre_friendly_name = genre_submitted_in_the_form
        new_genre = Genre()
        new_genre.name = new_genre_name
        new_genre.friendly_name = new_genre_friendly_name
        new_genre.save()
        updated_request.update({'genre': Genre.objects.get(name = new_genre.name).pk})
    
    format_submitted_in_the_form = updated_request['format']
    if(not format_submitted_in_the_form.isnumeric()):
        # Create a new label and insert it into the database
        new_format_name = format_submitted_in_the_form.lower()
        new_format_name = new_format_name.replace(" ", "_")
        new_format_friendly_name = format_submitted_in_the_form
        new_format = Format()
        new_format.name = new_format_name
        new_format.friendly_name = new_format_friendly_name
        new_format.save()
        updated_request.update({'format': Format.objects.get(name = new_format.name).pk})

    colour_submitted_in_the_form = updated_request['colour']
    if(not colour_submitted_in_the_form.isnumeric()):
        # Create a new label and insert it into the database
        new_colour_name = colour_submitted_in_the_form.lower()
        new_colour_name = new_colour_name.replace(" ", "_")
        new_colour_friendly_name = colour_submitted_in_the_form
        new_colour = Colour()
        new_colour.name = new_colour_name
        new_colour.friendly_name = new_colour_friendly_name
        new_colour.save()
        updated_request.update({'colour': Colour.objects.get(name = new_colour.name).pk})

    tags_submitted_in_the_form = updated_request.getlist('tags')
    for tag in tags_submitted_in_the_form:  
        if(not tag.isnumeric()):
            # Create a new label and insert it into the database
            new_tag_name = tag.lower()
            new_tag_name = new_tag_name.replace(" ", "_")
            new_tag_friendly_name = tag
            new_tag = Tag()
            new_tag.name = new_tag_name
            new_tag.friendly_name = new_tag_friendly_name
            new_tag.save()
            new_tag_index = tags_submitted_in_the_form.index(tag)
            tags_submitted_in_the_form[new_tag_index] = Tag.objects.get(name = new_tag.name).pk
            updated_request.setlist('tags', tags_submitted_in_the_form)

    return updated_request

def view_products(request):
    """ A view to show individual product details """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/view_products.html', context)

def view_product(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)
