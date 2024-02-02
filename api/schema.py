import strawberry
from strawberry.types import Info

from services.post import PostService
from services.author import AuthorService


async def get_author_posts(root: "AuthorType"):
    return await PostService.get_posts_by_author(author_id=root.id)


@strawberry.type
class AuthorType:
    id: strawberry.ID
    name: str
    posts: list["PostType"] = strawberry.field(resolver=get_author_posts)


@strawberry.type
class PostType:
    id: strawberry.ID
    title: str
    body: str
    author: "AuthorType"


@strawberry.type
class Query:
    @strawberry.field
    async def all_posts(self, info: Info) -> list[PostType]:
        return await PostService.get_all_posts()

    @strawberry.field
    async def all_authors(self, info: Info) -> list[AuthorType]:
        return await AuthorService.get_all_authors()


schema = strawberry.Schema(query=Query)
