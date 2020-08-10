from django.shortcuts import render


def index(request):
    context = {
        'judul': "Halaman Blog"
    }
    return render(request, 'home/index.html', context)
