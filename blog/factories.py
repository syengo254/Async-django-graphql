import random

import factory
from faker.providers import DynamicProvider

from .models import Author, Post


def author_provider_factory(elements):
    """Create the authors provider to attach to Faker"""
    authors_provider = DynamicProvider(
        provider_name="fake_author",
        elements=elements,
    )
    return authors_provider


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker("name")


AuthorFactory.create_batch(10000)

factory.Faker.add_provider(
    author_provider_factory(
        list(
            Author.objects.filter(
                pk__in=random.sample(range(3, Author.objects.count() - 1), 300)
            ).all()
        )
    )
)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    body = factory.Faker("text")
    author = factory.Faker("fake_author")
