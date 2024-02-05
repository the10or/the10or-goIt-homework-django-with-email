from django.contrib.auth.views import (PasswordResetConfirmView, PasswordResetDoneView,
                                       PasswordResetCompleteView)
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("reset-password/", views.ResetPasswordView.as_view(), name="password_reset"),
    path("reset-password/done/",
         PasswordResetDoneView.as_view(
             template_name="users/password_reset_done.html"
         ),
         name="password_reset_done"),

    path("reset-password/confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(
             template_name="users/password_reset_confirm.html",
             success_url="/users/reset-password/complete/"),
         name="password_reset_confirm"),

    path("reset-password/complete/",
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete"),

]
