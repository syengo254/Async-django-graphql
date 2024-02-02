from typing import Optional, List, TypeVar, Dict, Any, Generic

import strawberry
from strawberry.types import Info

from services.post import PostService
from services.author import AuthorService

import strawberry_django

from blog.models import Post, Author


Item = TypeVar("Item")


@strawberry.type
class PaginationWindow(Generic[Item]):
    items: List[Item] = strawberry.field(description="List of queried items.")
    items_count: int = strawberry.field(description="Number of total items in database.")


@strawberry_django.type(Author)
class AuthorType:
    id: strawberry.auto
    name: strawberry.auto
    posts: list["PostType"]
    posts_count: Optional[int]


@strawberry_django.type(Post)
class PostType:
    id: strawberry.auto
    title: strawberry.auto
    body: strawberry.auto
    author: "AuthorType"


@strawberry.type
class Query:
    @strawberry.field
    async def all_posts(
        self, info: Info, offset: Optional[int] = 0, limit: Optional[int] = 100
    ) -> PaginationWindow[PostType]:
        posts, count = await PostService.get_all_posts(offset, limit)
        return PaginationWindow(items=posts, items_count=count)

    @strawberry.field
    async def all_authors(
        self, info: Info, offset: Optional[int] = 0, limit: Optional[int] = 100
    ) -> PaginationWindow[AuthorType]:
        authors, count = await AuthorService.get_all_authors(
            offset, limit, with_count=True
        )
        return PaginationWindow(items=authors, items_count=count)


schema = strawberry.Schema(query=Query)
