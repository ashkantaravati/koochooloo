from django.shortcuts import render
from .models import Reference, Visit
from django.http import (
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)


def permamnent_redirect(request, id):
    ip = request.META.get("REMOTE_ADDR")
    user_agent = request.META.get("HTTP_USER_AGENT")
    requested_url = request.path
    outcome = None
    reference = None

    try:
        reference = Reference.objects.get(id=id)
        if not reference.is_active:
            outcome = HttpResponseNotFound()
        else:
            outcome = HttpResponsePermanentRedirect(reference.destination)

    except Reference.DoesNotExist:
        outcome = HttpResponseNotFound()

    Visit.objects.create(
        reference=reference,
        ip=ip,
        user_agent=user_agent,
        http_response_code=outcome.status_code,
        requested_url=requested_url,
    )
    return outcome
