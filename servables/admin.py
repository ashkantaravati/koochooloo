from django.contrib import admin
from .models import Servable


@admin.register(Servable)
class ServableAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "content_type",
        "url",
        "is_active",
        "updated_at",
    )
