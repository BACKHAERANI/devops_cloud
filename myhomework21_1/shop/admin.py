from django.contrib import admin

from shop.forms import ShopForm
from shop.models import Shop, Tag, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form = ShopForm


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
