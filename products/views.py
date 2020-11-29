from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ProductForm
from .models import Product, Artist, Label, Genre, Format, Colour, Tag
import re

# Create your views here.


@login_required
def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        updated_request = request.POST.copy()
        updated_request = add_dynamically_created_data_to_the_database(
            updated_request)
        form = ProductForm(updated_request, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

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
        updated_request.update(
            {'artist': Artist.objects.get(name=new_artist.name).pk})

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
        updated_request.update(
            {'label': Label.objects.get(name=new_label.name).pk})

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
        updated_request.update(
            {'genre': Genre.objects.get(name=new_genre.name).pk})

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
        updated_request.update(
            {'format': Format.objects.get(name=new_format.name).pk})

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
        updated_request.update(
            {'colour': Colour.objects.get(name=new_colour.name).pk})

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
            tags_submitted_in_the_form[new_tag_index] = Tag.objects.get(
                name=new_tag.name).pk
            updated_request.setlist('tags', tags_submitted_in_the_form)

    return updated_request


def view_products(request):
    """ A view to show individual product details """

    products = Product.objects.all()

    search_query = None
    sort = None
    direction = None
    _filter = None
    genre_filters = {}
    artist_filters = {}
    label_filters = {}
    format_filters = {}
    colour_filters = {}
    tag_filters = {}
    min_price = 0.00
    max_price = 300.00

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'filter' in request.GET:

            _filter = Q()
            filters = request.GET.getlist('filter')
            for filter in filters:
                filter_type = (re.search('t_(.*)=', filter)).group(1)
                filter_value = (re.search('=(.*)', filter)).group(1)
                if filter_type == "genre":
                    genre_filters[filter_value] = filter_value
                    _filter.add((Q(genre__name=filter_value)),
                                _filter.connector)
                if filter_type == "artist":
                    _filter.add((Q(artist__name=filter_value)),
                                _filter.connector)
                    artist_filters[filter_value] = filter_value
                if filter_type == "label":
                    _filter.add((Q(label__name=filter_value)),
                                _filter.connector)
                    label_filters[filter_value] = filter_value
                if filter_type == "format":
                    _filter.add((Q(format__name=filter_value)),
                                _filter.connector)
                    format_filters[filter_value] = filter_value
                if filter_type == "colour":
                    _filter.add((Q(colour__name=filter_value)),
                                _filter.connector)
                    colour_filters[filter_value] = filter_value
                if filter_type == "tag":
                    _filter.add((Q(tags__name=filter_value)),
                                _filter.connector)
                    tag_filters[filter_value] = filter_value
            products = products.filter(_filter)

        if 'price' in request.GET:
            price_range = request.GET['price']
            min_price = re.search('(.*)-', price_range).group(1)
            max_price = re.search('-(.*)', price_range).group(1)
            products = products.filter(price__range=(min_price, max_price))
            print(products)

        if 'artist' in request.GET:
            artist_request = request.GET['artist'].split(',')
            products = products.filter(artist__name__in=artist_request)
        if 'label' in request.GET:
            label_request = request.GET['label'].split(',')
            products = products.filter(label__name__in=label_request)
        if 'genre' in request.GET:
            genre_request = request.GET['genre'].split(',')
            products = products.filter(genre__name__in=genre_request)

        if 'tag' in request.GET:
            tag_request = request.GET['tag'].split(',')
            products = products.filter(tags__name__in=tag_request)

        if 'search_bar_main' in request.GET:
            search_query = request.GET['search_bar_main']
            if not search_query:
                return redirect(reverse('view_products'))

            search_queries = (Q(name__icontains=search_query) |
                              Q(artist__name__icontains=search_query) |
                              Q(label__name__icontains=search_query) |
                              Q(description__icontains=search_query) |
                              Q(tracklist__icontains=search_query)
                              )
            products = products.filter(search_queries)

    context = {
        'products': products,
        'genre_filters': genre_filters,
        'artist_filters': artist_filters,
        'label_filters': label_filters,
        'format_filters': format_filters,
        'colour_filters': colour_filters,
        'tag_filters': tag_filters,
        'min_price': min_price,
        'max_price': max_price,
    }

    return render(request, 'products/view_products.html', context)


def view_product(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)
