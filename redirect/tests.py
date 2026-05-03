from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import Reference, Visit


class ReferenceModelTests(TestCase):
    def test_short_url_properties_and_total_visits(self):
        reference = Reference.objects.create(
            title="Docs",
            destination="https://example.com/docs",
            is_active=True,
        )
        Visit.objects.create(
            reference=reference,
            requested_url=f"/r/{reference.id}/",
            user_agent="pytest",
            http_response_code=301,
        )

        self.assertTrue(reference.short_url.endswith(f"/r/{reference.id}"))
        self.assertEqual(
            reference.short_url_with_protocol_http,
            f"http://{reference.short_url}",
        )
        self.assertEqual(
            reference.short_url_with_protocol_https,
            f"https://{reference.short_url}",
        )
        self.assertEqual(reference.total_visits, 1)


class RedirectViewTests(TestCase):
    def test_active_reference_redirects_and_logs_visit(self):
        reference = Reference.objects.create(
            title="Active",
            destination="https://example.com",
            is_active=True,
        )

        response = self.client.get(
            f"/r/{reference.id}/",
            HTTP_USER_AGENT="browser",
            HTTP_X_FORWARDED_FOR="203.0.113.2",
        )

        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], "https://example.com")
        visit = Visit.objects.get(reference=reference)
        self.assertEqual(visit.http_response_code, 301)
        self.assertEqual(visit.ip, "203.0.113.2")

    def test_inactive_reference_returns_404_and_logs_visit(self):
        reference = Reference.objects.create(
            title="Inactive",
            destination="https://example.com",
            is_active=False,
        )

        response = self.client.get(f"/r/{reference.id}/", HTTP_USER_AGENT="browser")

        self.assertEqual(response.status_code, 404)
        visit = Visit.objects.get(reference=reference)
        self.assertEqual(visit.http_response_code, 404)


class ReferenceApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_references_is_public(self):
        reference = Reference.objects.create(
            title="Public",
            destination="https://example.com",
        )

        response = self.client.get("/api/references")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], reference.title)

    def test_create_reference_requires_authentication(self):
        payload = {
            "title": "new",
            "destination": "https://example.com/new",
            "is_active": True,
        }

        unauth_response = self.client.post("/api/references", payload, format="json")
        self.assertEqual(unauth_response.status_code, 403)

        user = get_user_model().objects.create_user("apiuser", password="password123")
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.key}")
        auth_response = self.client.post("/api/references", payload, format="json")

        self.assertEqual(auth_response.status_code, 201)
        self.assertEqual(Reference.objects.count(), 1)
