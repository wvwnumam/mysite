from django.urls import path
from .views import PostListView, IndexView, PostDetailView, PostFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:category>', PostListView.as_view(), name='category'),
    path('<str:category>/<int:page>', PostListView.as_view(), name='category'),
    path('p/<slug:slug>', PostFormView.as_view(), name="post")
]