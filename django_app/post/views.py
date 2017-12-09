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


def post_detail(request):
    pass


def post_create(request):
    pass


def post_modify(request):
    pass


def post_delete(request):
    pass

