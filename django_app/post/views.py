from django.http import HttpResponse
from django.shortcuts import render

from post.models import Post


def index(request):
    return HttpResponse('Hello, world')


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)

def post_create(request):
    pass


def post_modify(request, post_pk):
    pass


def post_delete(request, post_pk):
    pass

