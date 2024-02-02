import asyncio

from asgiref.sync import sync_to_async

from django.db.models import Count

from .models import Author, Post


class AuthorRepository:
    @staticmethod
    async def get_all_authors(
        offset: int, limit: int, with_count=False
    ) -> tuple[list[Author], int]:
        if with_count is False:
            author_queryset = Author.objects.prefetch_related("posts").order_by("-id")
        else:
            author_queryset = Author.objects.prefetch_related("posts").annotate(
                posts_count=Count("posts__pk"),
            )

        authors, count = await asyncio.gather(
            *[
                sync_to_async(list)(author_queryset.all()[offset : offset + limit]),
                Post.objects.acount(),
            ]
        )
        return authors, count


class PostRepository:
    @staticmethod
    async def get_all_posts(offset: int, limit: int) -> tuple[
        list[Post],
        int,
    ]:
        posts, count = await asyncio.gather(
            *[
                sync_to_async(list)(
                    Post.objects.select_related("author").all()[offset : offset + limit]
                ),
                Post.objects.acount(),
            ]
        )
        return posts, count

    @staticmethod
    async def get_posts_by_author(author_id: int) -> list[Post]:
        posts = [
            post
            async for post in Post.objects.select_related("author")
            .filter(author_id=author_id)
            .all()
        ]
        return posts
