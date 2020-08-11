from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title

