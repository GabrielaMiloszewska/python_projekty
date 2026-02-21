import pytest
from blog.factories import PostFactory

@pytest.mark.django_db
class PostModelTest:


    @pytest.mark.parametrize(
        "content,length",
        [
            ("ABC", 3),
            ("ABC123", 6),
            ("A  B C 1 2  3", 13),
            ("   A  B C 1 2  3    ", 20),
        ]
    )
    def test_length_method(self, content, length):
        p = PostFactory.build(content=content)
        assert p.length() == length


    def test_get_snippet_short_text(self):
        content = "Hello world"
        p = PostFactory.build(content=content)

        assert p.get_snippet() == content

    def test_get_snippet_long_text(self):
        long_text = "A" * 150
        p = PostFactory.build(content=long_text)

        snippet = p.get_snippet()

        assert len(snippet) <= 103
        assert snippet.endswith("...")
        assert snippet.startswith("A" * 100)