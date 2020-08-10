from django.shortcuts import render


def index(request):
    context = {
        'judul': "Halaman blog"
    }
    return render(request, 'home/index.html', context)
