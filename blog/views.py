from django.shortcuts import render
from .models import Post

def categories():
    return Post.objects.values('category').distinct()

def index(request):
    # Queryset
    posts = Post.objects.all().order_by('publish').reverse()

    context = {
        'title': "Selamat Datang di MySite",
        'categories': categories(),
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def category(request, category):
    # Queryset
    posts = Post.objects.filter(category=category).order_by('publish').reverse()

    context = {
        'title': "Kategori",
        'categories': categories(),
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def post(request, slug):
    # Queryset
    post = Post.objects.get(slug=slug)

    context = {
        'title': post.title,
        'categories': categories(),
        'post': post
    }
    return render(request, 'blog/post.html', context)