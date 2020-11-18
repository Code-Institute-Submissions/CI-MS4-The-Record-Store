from django.shortcuts import render

# Create your views here.


@login_required
def profile(request):
    
    template = 'profiles/profile.html'
    context = {

    }

    return render(request, template, context)