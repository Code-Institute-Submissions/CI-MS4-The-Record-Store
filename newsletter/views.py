from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Subscriber

# Create your views here.


def sign_up_to_newsletter(request):
    """ Sign Up For Newsletter """

    print(request.POST)
    email_address = request.POST.get('email')

    try:
        validate_email(email_address)
    except ValidationError as e:
        messages.error(request, f'Sorry you entered an invalid email. {e}')
    else:
        # Check if the email address is already on the subscriber list
        if Subscriber.objects.filter(email=email_address).exists():
            messages.success(
                request, 'You are already signed up for our newsletter!')
        else:
            new_subscriber = Subscriber()
            new_subscriber.email = email_address
            new_subscriber.save()
            messages.success(
                request, 'Thank you for signing up for our newsletter!')

    return redirect(reverse('home'))
