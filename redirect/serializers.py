from rest_framework import serializers

from redirect.models import Reference


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = (
            "title",
            "destination",
            "is_active",
            "description",
            "short_url",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "short_url",
            "created_at",
            "updated_at",
        )
