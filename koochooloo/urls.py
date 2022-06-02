from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from redirect import views, apis

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"references/?", apis.ReferenceViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("r/<str:id>", views.permamnent_redirect, name="redirect"),
    path("api/", include(router.urls)),
]
