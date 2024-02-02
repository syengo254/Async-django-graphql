from .models import Author, Post


class AuthorRepository:
    @staticmethod
    async def get_all_authors() -> list[Author]:
        authors = [
            author
            async for author in Author.objects.prefetch_related("posts")
            .order_by("-id")
            .all()
        ]
        return authors


class PostRepository:
    @staticmethod
    async def get_all_posts() -> list[Post]:
        posts = [post async for post in Post.objects.select_related("author").all()]
        return posts

    @staticmethod
    async def get_posts_by_author(author_id: int) -> list[Post]:
        posts = [
            post
            async for post in Post.objects.select_related("author")
            .filter(author_id=author_id)
            .all()
        ]
        return posts
