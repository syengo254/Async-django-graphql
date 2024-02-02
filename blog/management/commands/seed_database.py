from time import sleep

from django.core.management.base import BaseCommand

from blog.factories import PostFactory


class Command(BaseCommand):
    help = "Seed the database with millions of records."

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.NOTICE("Generating 1 million posts, please wait..."),
        )

        try:
            for i in range(1000):
                _ = PostFactory.create_batch(1000)
                sleep(0.01)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"{e}"))

        self.stdout.write(
            self.style.SUCCESS("Done Generating 1 million posts."),
        )
