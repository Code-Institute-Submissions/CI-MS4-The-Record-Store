from django.shortcuts import render
from .forms import OrderForm
from profiles.models import UserProfile
# Create your views here.


def checkout(request):

    if request.method == 'POST':
        print('post')
    else:
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            print(user_profile.primary_address)
            user_primary_address = user_profile.primary_address
            order_form = OrderForm(instance=user_primary_address)
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
