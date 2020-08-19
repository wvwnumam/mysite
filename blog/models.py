from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    slug = models.SlugField()
    image = models.CharField(max_length=500)
    publish = models.DateTimeField( auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_slug = models.SlugField()
    author = models.CharField(max_length=50, default='anonymous')
    text = models.TextField()
    publish = models.DateTimeField( auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.publish.strftime('%Y-%m-%d %H:%M:%S')

