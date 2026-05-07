from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from hashid_field.field import HashidAutoField

BASE_HOST = settings.BASE_HOST


class Reference(models.Model):
    id = HashidAutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name=_("Title"))
    destination = models.URLField(verbose_name=_("Destination URL"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Reference")
        verbose_name_plural = _("References")

    @property
    def short_url(self):
        return f"{BASE_HOST}/r/{self.id}"

    @property
    def short_url_with_protocol_http(self):
        return f"http://{self.short_url}"

    @property
    def short_url_with_protocol_https(self):
        return f"https://{self.short_url}"

    @property
    def total_visits(self):
        return self.visits.count()

    def __str__(self):
        return f"Reference #{self.id}({self.title})"


class Visit(models.Model):
    id = HashidAutoField(primary_key=True)
    reference = models.ForeignKey(
        Reference,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="visits",
        verbose_name=_("Reference"),
    )
    requested_url = models.CharField(max_length=255, verbose_name=_("Requested URL"))
    ip = models.GenericIPAddressField(null=True, verbose_name=_("IP"))
    user_agent = models.CharField(max_length=255, verbose_name=_("User agent"))
    http_response_code = models.IntegerField(
        default=200,
        verbose_name=_("HTTP response code"),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Visit")
        verbose_name_plural = _("Visits")

    def __str__(self):
        return f"Visit #{self.id}({self.reference})"
