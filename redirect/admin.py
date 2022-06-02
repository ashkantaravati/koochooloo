from django.contrib import admin
from .models import Reference, Visit


class VisitTabularInline(admin.TabularInline):
    model = Visit
    extra = 0
    readonly_fields = (
        "id",
        "ip",
        "user_agent",
        "requested_url",
        "http_response_code",
        "created_at",
    )
    ordering = ("-created_at",)
    can_delete = False


@admin.register(Reference)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "short_url_with_protocol_http",
        "short_url_with_protocol_https",
        "destination",
        "is_active",
        "total_visits",
        "updated_at",
    )
    inlines = [VisitTabularInline]


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ip",
        "user_agent",
        "requested_url",
        "http_response_code",
        "reference",
        "created_at",
    )


admin.site.site_title = "Koochooloo URL Redirection Tool"
admin.site.site_header = "Koochooloo URL Redirection Tool"
