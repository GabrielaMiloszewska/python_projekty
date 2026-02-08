from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .services import service
from .forms import AuthorForm, NewsForm


# Create your views here.
def news_list(request):
    return render(request, 'news/list.html', {'news': service.get_news()})


def news_details(request, pk):
    return render(request, 'news/details.html', {'news': service.get_by_id(pk)})


@login_required
def author_add(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, 'Successfully Added!')

    return render(
        request,
        template_name="news/author_form.html",
        context={"form": form}
    )
