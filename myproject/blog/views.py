from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .services import blog

import logging

logger = logging.getLogger(__name__)


class PostListView(ListView):
    model = Post
    template_name = "blog/list.html"
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.info(
            f"Pobieram stronę: {self.request.GET.get('page')} "
            f"z {context['paginator'].num_pages}"
        )
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/details.html"
    pk_url_kwarg = "id"
    context_object_name = "post" # to chyba zbędne
