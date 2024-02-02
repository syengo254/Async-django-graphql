from blog.repositories import PostRepository


class PostService:
    @staticmethod
    async def get_all_posts():
        return await PostRepository.get_all_posts()

    @staticmethod
    async def get_posts_by_author(author_id: int):
        return await PostRepository.get_posts_by_author(author_id)
