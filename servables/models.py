from django.db import models
from django.conf import settings
from django.forms import URLField

BASE_HOST = settings.BASE_HOST
from hashid_field.field import HashidAutoField

CONTENT_TYPE_CHOICES = [
    ("text/css", "CSS (text/css)"),
    ("text/csv", "CSV (text/csv)"),
    ("text/html", "HTML (text/html)"),
    ("text/plain", "Plain Text (text/plain)"),
    ("text/xml", "XML (text/xml)"),
    ("application/javascript", "JavaScript (application/javascript)"),
    ("application/xml", "XML (application/xml)"),
    ("application/json", "JSON (application/json)"),
]


class Servable(models.Model):
    id = HashidAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    content_type = models.CharField(choices=CONTENT_TYPE_CHOICES, max_length=150)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return f"http://{BASE_HOST}/servable/{self.id}"
