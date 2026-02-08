from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="list"),
    path("post/<int:id>/", views.post_details, name="details"),
]