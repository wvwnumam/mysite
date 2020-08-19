from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'update', 'publish')
    search_fields = ('title', 'body', 'author')
    readonly_fields = ['slug', 'publish', 'update']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post_slug', 'author', 'text', 'update', 'publish')
    search_fields = ('author', 'text')
    readonly_fields = ['publish', 'update']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_header = 'Administration'