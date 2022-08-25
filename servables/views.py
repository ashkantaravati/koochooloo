from django.http import HttpResponseNotFound
from django.shortcuts import HttpResponse, get_object_or_404

from .models import Servable


def serve_servable(request, id):
    servable = get_object_or_404(Servable, pk=id)
    if not servable.is_active:
        return HttpResponseNotFound()
    return HttpResponse(
        servable.content, headers={"Content-Type": servable.content_type}
    )
