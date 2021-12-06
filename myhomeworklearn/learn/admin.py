from django.contrib import admin
from learn.models import Show


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "created_at"]
    list_display_links = ["name"]


