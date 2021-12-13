from django.contrib import admin
from shop.models import Shop, Tag, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
