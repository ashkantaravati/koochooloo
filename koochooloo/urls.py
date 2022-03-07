from django.contrib import admin
from django.urls import path

from redirect.views import permamnent_redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("r/<str:id>", permamnent_redirect, name="redirect"),
]
