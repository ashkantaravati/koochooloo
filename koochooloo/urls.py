from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from redirect.apis import ReferenceViewSet

# from redirect import views, apis
from redirect.views import permanent_redirect
from servables.views import serve_servable

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"references/?", ReferenceViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("r/<str:id>/", permanent_redirect, name="redirect"),
    path("servable/<str:id>/", serve_servable, name="serve_servable"),
    path("api/", include(router.urls)),
]
