from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RedirectConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "redirect"
    verbose_name = _("Redirects")
