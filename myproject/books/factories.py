import factory
from .models import Book

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    id = factory.Sequence(lambda n: n)
    title = factory.Faker('sentence')
    author = factory.Faker('name')
    year = factory.Faker('year')
    description = factory.Faker('sentence')
    price = factory.Faker('random_float')