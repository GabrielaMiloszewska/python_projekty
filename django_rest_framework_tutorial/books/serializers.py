from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', "books")


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='book-highlight', format='html')
    class Meta:
        model = Book
        fields = ["url", "id", "title", "author", "status", "visible", "created", # zamiast wypisywać tych pól możnaby wpisać: __all__
            "code", "linenos", "language", "style", "owner", 'highlight',]
        read_only_fields = ["id", "created"]