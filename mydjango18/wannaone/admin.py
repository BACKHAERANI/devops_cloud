from django.contrib import admin
from wannaone.models import Star, Comment, Tag


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

