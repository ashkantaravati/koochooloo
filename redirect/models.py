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

    def __str__(self):
        return f"Reference #{self.id}({self.title})"
