from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="index_page"),
    path("details/<author_id>/", views.details, name="author_details"),
    path("authors/", views.author_list, name="author_list"),
    path("tag/<tag>", views.tag_list, name="tag_list"),
]
