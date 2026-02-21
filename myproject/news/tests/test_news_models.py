import pytest
from django.contrib.auth.models import User
from news.models import Author, News, Tag


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser",
        password="test123"
    )


@pytest.mark.django_db
class TestNewsModels:

    def test_author_short_name(self, user):
        author = Author.objects.create(
            first_name="Janusz",
            last_name="Januszewski",
            created_by=user
        )

        assert author.short_name == "JJ"

    def test_author_str(self, user):
        author = Author.objects.create(
            first_name="Tomasz",
            last_name="Tomaszewski",
            created_by=user
        )

        assert str(author) == "Tomasz Tomaszewski"

    def test_tag_slug_generation(self):
        tag = Tag.objects.create(name="Ładny Test")
        assert tag.slug == "ladny-test"