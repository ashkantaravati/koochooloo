from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from redirect.models import Reference
from redirect.serializers import ReferenceSerializer


class BearerTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"


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
    short_url_with_protocol_http -- short_url with protocol http prepended. read-only.
    short_url_with_protocol_https -- short_url with protocol https prepended. read-only.
    created_at -- The date and time the reference was created. read-only.
    updated_at -- The date and time the reference was last updated. read-only.

    """

    authentication_classes = [SessionAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
