from django.contrib import admin
from post.models import Language, Electronics, Post, Comment

admin.site.register(Language)
admin.site.register(Electronics)
admin.site.register(Post)
admin.site.register(Comment)