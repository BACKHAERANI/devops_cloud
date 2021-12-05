from django.contrib import admin
from hwangridangil.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ["id","name","description","telephone"]
    list_display_links = ["name"]


admin.site.register(Shop, ShopAdmin)