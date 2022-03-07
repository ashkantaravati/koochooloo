from django.shortcuts import render
from .models import Reference
from django.http import (
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)


def permamnent_redirect(request, id):
    reference = Reference.objects.get(id=id)
    if reference is None:
        return HttpResponseNotFound()
    if not reference.is_active:
        return HttpResponseNotFound()
    return HttpResponsePermanentRedirect(reference.destination)
