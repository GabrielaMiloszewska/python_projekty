from news.models import Author, News

def my_context(request):
    return {
        "redakcja": "alx.pl"
    }


def global_metrics(request):
    return {
        "ilosc_autorow": Author.objects.count(),
        "ilosc_newsow": News.objects.count(),
    }