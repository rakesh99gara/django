from django.contrib import admin

from blogs.models import Post,Comment,Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)

# Register your models here.
