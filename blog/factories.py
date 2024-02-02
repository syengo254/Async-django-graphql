import random

import factory


from factory import Faker
from faker.providers import DynamicProvider

from .models import Author, Post


authors_provider = DynamicProvider(
    provider_name="fake_author",
    elements=list(
        Author.objects.filter(
            pk__in=random.sample(range(3, Author.objects.count() - 1), 300)
        ).all()
    ),
)

Faker.add_provider(authors_provider)


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker("name")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=12)
    body = factory.Faker("text")
    author = factory.Faker("fake_author")
