from django.contrib import admin
from blog.models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "created_at"]
    list_display_links = ["title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["pk", "post", "message", "created_at"]
    list_display_links = ["post"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
