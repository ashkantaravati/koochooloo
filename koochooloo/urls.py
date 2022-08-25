import imp
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# from redirect import views, apis
from redirect.views import permamnent_redirect
from redirect.apis import ReferenceViewSet
from servables.views import serve_servable

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"references/?", ReferenceViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("r/<str:id>/", permamnent_redirect, name="redirect"),
    path("servable/<str:id>/", serve_servable, name="serve_servable"),
    path("api/", include(router.urls)),
]
