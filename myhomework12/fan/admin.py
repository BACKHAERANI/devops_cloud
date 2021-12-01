from django.contrib import admin
from fan.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "fan_name", "created_at"]
    search_fields = ["title"]


admin.site.register(Post, PostAdmin)

#from django.contrib import admin

# Register your models here.
