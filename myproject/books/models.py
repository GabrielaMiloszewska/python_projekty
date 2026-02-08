from dataclasses import dataclass
from faker import Faker

faker = Faker("pl_PL")

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    description: str
    price: float

    def length(self):
        return len(self.description)

    @classmethod
    def fake(cls, id):
        return cls(
            id=id,
            title=faker.sentence(nb_words=3),
            author=faker.name(),
            year=faker.year(),
            description=faker.paragraph(nb_sentences=5),
            price=round(faker.pyfloat(min_value=10, max_value=120), 2),
        )

    @property
    def snippet(self):
        return self.description[:100] + "..."

# Create your models here.
class DummyDb:
    def __init__(self):
        self.books: list[Book] = []

    def generate_n_fake_books(self, n: int):
        for i in range(n):
            self.books.append(Book.fake(i))

    def all(self):
        return self.books

    def get(self, id):
        return next(filter(lambda book: book.id == id, self.books))


class BookService:
    def __init__(self, db: DummyDb):
        self.db = db

    def get_books(self):
        return self.db.all()

    def get_book(self, id):
        return self.db.get(id)

db = DummyDb()
db.generate_n_fake_books(100)

book_service = BookService(db)