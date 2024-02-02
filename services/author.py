from blog.repositories import AuthorRepository


class AuthorService:
    @staticmethod
    async def get_all_authors(offset, limit, with_count=False):
        return await AuthorRepository.get_all_authors(
            offset, limit, with_count=with_count
        )
