from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name[:25]


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts", null=True
    )

    def __str__(self) -> str:
        return self.title[:25]
