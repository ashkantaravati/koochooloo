from django.test import TestCase

from .models import Servable


class ServableModelTests(TestCase):
    def test_string_representation(self):
        servable = Servable.objects.create(
            title="about",
            content="hello",
            content_type="text/plain",
            is_active=True,
        )

        self.assertTrue(servable.url.endswith(f"/servable/{servable.id}"))
        self.assertEqual(servable.content_type, "text/plain")
