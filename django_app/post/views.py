from django.http import HttpResponse
from django.shortcuts import render

from post.models import Post


def index(request):
    return HttpResponse('Hello, world')


def post_list(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'post/post_list.html', context)
