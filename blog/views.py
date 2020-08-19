from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views import View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Categories for navbar
categories = Post.objects.values('category').distinct()

class PostListView(ListView):
    model = Post
    ordering = 'publish'
    paginate_by = 2
    template_name = 'blog/category.html'
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


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    extra_context = {
        'title': 'Unggahan',
        'categories': categories,
        'form': CommentForm,
    }

    def get_context_data(self, **kwargs):
        comments = Comment.objects.filter(post_slug=self.kwargs['slug']) # get comment
        self.kwargs.update(self.extra_context)
        self.kwargs.update({'comments': comments})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class PostFormView(FormView):
    template_name = 'blog/post.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        post = Post.objects.get(slug=self.kwargs['slug']) # get single post
        comments = Comment.objects.filter(post_slug=self.kwargs['slug']).order_by('publish').reverse() # get comment

        context = super().get_context_data(**kwargs)
        context['title'] = 'Unggahan'
        context['categories'] = categories
        context['post'] = post
        context['comments'] = comments

        return context

    def post(self, request, *args, **kwargs):
        comment = Comment()
        comment.post_slug = kwargs['slug']
        comment.text = request.POST.get('text')
        comment.save()

        return HttpResponseRedirect('/p/' + self.kwargs['slug'])    
