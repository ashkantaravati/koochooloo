from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from hashid_field.field import HashidAutoField

BASE_HOST = settings.BASE_HOST

CONTENT_TYPE_CHOICES = [
    ("text/css", _("CSS (text/css)")),
    ("text/csv", _("CSV (text/csv)")),
    ("text/html", _("HTML (text/html)")),
    ("text/plain", _("Plain Text (text/plain)")),
    ("text/xml", _("XML (text/xml)")),
    ("application/javascript", _("JavaScript (application/javascript)")),
    ("application/xml", _("XML (application/xml)")),
    ("application/json", _("JSON (application/json)")),
]


class Servable(models.Model):
    id = HashidAutoField(primary_key=True)
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))
    content_type = models.CharField(
        choices=CONTENT_TYPE_CHOICES,
        max_length=150,
        verbose_name=_("Content type"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Servable")
        verbose_name_plural = _("Servables")

    @property
    def url(self):
        return f"http://{BASE_HOST}/servable/{self.id}"
