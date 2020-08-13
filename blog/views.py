from django.shortcuts import render
from .models import Post


def index(request):
    # Queryset
    posts = Post.objects.all().order_by('date_created').reverse()

    context = {
        'title': "Selamat Datang di MySite",
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def category(request, category):
    # Queryset
    posts = Post.objects.filter(category=category).order_by('date_created').reverse()

    context = {
        'title': "Kategori",
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def post(request, slug):
    # Queryset
    post = Post.objects.get(slug=slug)

    context = {
        'title': post.title,
        'post': post
    }
    return render(request, 'blog/post.html', context)