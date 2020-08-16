from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

# Categories for navbar
categories = Post.objects.values('category').distinct()

class PostListView(ListView):
    model = Post
    ordering = 'publish'
    paginate_by = 2
    template_name = "blog/category.html"
    extra_context = {
        'title': 'Selamat Datang di MySite',
        'categories': categories
    }

    def get_queryset(self):
        if self.kwargs['category'] != 'all':
            self.queryset = self.model.objects.filter(category=self.kwargs['category'])
            self.kwargs.update({'category': self.kwargs['category']})
        return super().get_queryset().order_by('publish').reverse()
    
    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)
    

class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.all().order_by('publish').reverse() # All post
        newest = Post.objects.all().order_by('publish').reverse()[:3] # Newest post

        context = super().get_context_data(**kwargs)
        context['title'] = 'Selamat Datang di Mysite'
        context['categories'] = categories
        context['posts'] = posts
        context['newest'] = newest
        
        return context

class PostView(TemplateView):
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        # get single post by slug
        post = Post.objects.get(slug=kwargs['slug'])

        context = super().get_context_data(**kwargs)
        context['title'] = post.title
        context['categories'] = categories
        context['post'] = post
        
        return context