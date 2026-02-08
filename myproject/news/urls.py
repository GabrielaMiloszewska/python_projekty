from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('news/', views.news_list, name='list'),
    path('news/<int:pk>/', views.news_details, name='details'),
    path("news/author/add/", views.author_add, name="author_add"),
]