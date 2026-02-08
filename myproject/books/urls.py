from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.book_list, name="list"),
    path("book/<int:id>/", views.book_details, name="details"),
]