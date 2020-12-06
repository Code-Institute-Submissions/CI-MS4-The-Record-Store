from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()
    new_releases = products.filter(tags__name='new_release')
    special_offers = products.filter(tags__name='three_for_two')

    print(new_releases)
    print(special_offers)
    context = {
        'new_releases': new_releases,
        'special_offers': special_offers,
    }

    return render(request, 'home/index.html', context)
