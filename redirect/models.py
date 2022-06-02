from django.db import models
from hashid_field.field import HashidAutoField
from django.conf import settings

BASE_HOST = settings.BASE_HOST


class Reference(models.Model):
    id = HashidAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    destination = models.URLField()
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    )
    requested_url = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    http_response_code = models.IntegerField(default=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Visit #{self.id}({self.reference})"
