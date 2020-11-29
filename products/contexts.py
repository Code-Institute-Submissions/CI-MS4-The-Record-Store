from products.models import Genre, Format, Artist, Colour, Label, Tag


def product_sub_models(request):

    formats = Format.objects.all()
    genres = Genre.objects.all()
    artists = Artist.objects.all()
    colours = Colour.objects.all()
    labels = Label.objects.all()
    tags = Tag.objects.all()

    context = {
        'formats': formats,
        'genres': genres,
        'artists': artists,
        'colours': colours,
        'labels': labels,
        'tags': tags,
    }
    return context
