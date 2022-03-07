from django.contrib import admin
from .models import Reference


@admin.register(Reference)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "short_url",
        "destination",
        "is_active",
        "updated_at",
    )


admin.site.site_title = "Koochooloo URL Redirection Tool"
admin.site.site_header = "Koochooloo URL Redirection Tool"
