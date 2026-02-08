from django.shortcuts import render
from .models import book_service
from django.core.paginator import Paginator

# Create your views here.
def book_list(request):

    paginator = Paginator(book_service.get_books(), 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "books/list.html", {"page_obj": page_obj})


def book_details(request, id):
    book = book_service.get_book(id)

    return render(request, "books/details.html", {"book": book})