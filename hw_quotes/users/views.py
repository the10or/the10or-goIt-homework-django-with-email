from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import SignUpForm, LoginForm, ProfileForm


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


def profile_view(request):
    if request.method == "POST":
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile updated")
            return redirect(to="users:profile")

    profile_form = ProfileForm(instance=request.user.profile)
    return render(
        request,
        "users/profile.html",
        context={"profile_form": profile_form}
    )


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    html_email_template_name = "users/password_reset_email.html"
    success_url = reverse_lazy("users:password_reset_done")
    success_message = "Check your email to reset your password"
    subject_template_name = "users/password_reset_subject.txt"