from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    prepopulated_fields = {"slug": ("title",)}
