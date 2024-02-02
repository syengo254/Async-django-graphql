from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Post

# Create your views here.


async def index(request):
    post = await Post.objects.filter(pk=1).afirst()

    return HttpResponse(post.title)
