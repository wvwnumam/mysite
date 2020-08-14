from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'update', 'publish')
    search_fields = ('title', 'body', 'author')
    readonly_fields = ['slug', 'publish', 'update']

admin.site.register(Post, PostAdmin)

admin.site.site_header = 'Administration'