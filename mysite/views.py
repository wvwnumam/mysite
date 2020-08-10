from django.shortcuts import render


def index(request):
    context = {
        'judul': "Halaman Home"
    }
    return render(request, 'home/index.html', context)
