from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('c/<str:category>', views.category, name="category"),
    path('p/<slug:slug>', views.post, name="post")
]