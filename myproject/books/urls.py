from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.book_list, name="list"),
    path("create/", views.BookCreateView.as_view(), name="create"),
    path("book/<int:id>/", views.book_details, name="details"),
]