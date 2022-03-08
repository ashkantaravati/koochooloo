from rest_framework import viewsets, mixins

from redirect.models import Reference
from redirect.serializers import ReferenceSerializer


class ReferenceViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    API endpoint that allows external systems to create, list, and retrieve references.
    title -- The title of the reference. required
    destination -- The destination of the reference. Should be a valid URL. required
    is_active -- Whether or not the reference is active. Optional.
    description -- A description of the reference. Optional.
    short_url -- The resulting short URL for the reference, created with the configured BASE_HOST and hashid generated for this reference automatically. read-only.
    created_at -- The date and time the reference was created. read-only.
    updated_at -- The date and time the reference was last updated. read-only.

    """

    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
