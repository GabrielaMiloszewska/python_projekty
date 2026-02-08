from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import HelloUserNameHistory
def index(request):
    return render(
        request,
        "simplerouting/index.html",
        {"text": "Hello in Django ALX Course"}
    )


def hello(request, username=""):

    if username:
        text = f"Hello {username}"
        HelloUserNameHistory(username=username).save()

    else:
        text = "Hello World"

    return HttpResponse(text)

all_books = [
    {"title": "My first book", "author": "XYZ"},
    {"title": "My second book", "author": "ABC"},
    {"title": "My third book", "author": "GFT"},]

def books_list(request):
    return render(request, "simplerouting/books.html", {"books": all_books})