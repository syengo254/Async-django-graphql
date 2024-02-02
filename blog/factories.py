import random

import factory

from .models import Author, Post


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker("name")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    body = factory.Faker("text")
    author = Author.objects.filter(
        pk=random.randint(11, Author.objects.count() - 1)
    ).first()
