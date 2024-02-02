from blog.repositories import PostRepository


class PostService:
    @staticmethod
    async def get_all_posts(offset, limit):
        return await PostRepository.get_all_posts(offset, limit)

    @staticmethod
    async def get_posts_by_author(author_id: int, offset, limit):
        return await PostRepository.get_posts_by_author(
            author_id,
            offset,
            limit,
        )
