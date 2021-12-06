from django.contrib import admin
from hrdan.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at"]
    list_display_links = ["name"]
