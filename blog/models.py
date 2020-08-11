from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    date_created = models.DateTimeField( auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

