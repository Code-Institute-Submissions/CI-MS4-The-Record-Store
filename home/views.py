from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """

    products = Product.objects.all()
    new_releases = products.filter(tags__name='new_release')
    recommended = products.filter(tags__name='recommended')

    context = {
        'new_releases': new_releases,
        'recommended_products': recommended,
    }

    return render(request, 'home/index.html', context)
