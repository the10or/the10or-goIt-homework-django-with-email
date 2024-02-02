from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect(to="users:login")

        login(request, user)
        return redirect("/")

    return render(request, "users/login.html", context={"form": LoginForm()})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "users/signup.html", context={"form": form})

    return render(request, "users/signup.html", context={"form": SignUpForm()})


def profile_view(request, user):
    return request, "users/profile.html"