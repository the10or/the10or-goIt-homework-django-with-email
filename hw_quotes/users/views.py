from django.shortcuts import render


# Create your views here.
def login_view(request):
    return render(request, 'users/login.html', context={})


def signup_view(request):
    return render(request, 'users/signup.html', context={})


def logout_view(request):
    return render(request, 'users/logout.html', context={})
