from django.shortcuts import render
from .models import Post


def index(request):
    # Queryset
    posts = Post.objects.all()

    context = {
        'judul': "Halaman Utama",
        'posts': posts
    }
    return render(request, 'blog/index.html', context)
