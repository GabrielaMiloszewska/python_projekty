import pytest
from django.urls import reverse
from blog.factories import PostFactory

@pytest.mark.django_db
def test_post_list_view(client):
    url = reverse("blog:list")

    response = client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
def test_post_details_view(client):
    post = PostFactory.create()

    url = reverse("blog:details", args=[post.id])

    response = client.get(url)

    assert response.status_code == 200
    assert post.title in response.content.decode()

@pytest.mark.django_db
def test_list_page_contains_post_title(client):
    posts = PostFactory.create_batch(3)
    url = reverse("blog:list")
    response = client.get(url)

    for post in posts:
        assert post.title in response.content.decode()

    assert response.status_code == 200
    assert len(posts) == response.context["page_obj"].paginator.count