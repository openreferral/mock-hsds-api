import unittest
from unittest.mock import patch
from uuid import uuid4

import app


class ServiceDetailEndpointTests(unittest.TestCase):
    def setUp(self):
        app.app.config["TESTING"] = True
        self.client = app.app.test_client()

    def test_returns_service_content_for_existing_service(self):
        service_id = uuid4()
        service = {"id": str(service_id), "name": "Example service"}

        with patch.object(
            app,
            "get_file_contents_from_uuid_in_directory",
            return_value=service,
        ):
            response = self.client.get(f"/services/{service_id}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), service)

    def test_returns_404_for_missing_service(self):
        service_id = uuid4()

        with patch.object(
            app,
            "get_file_contents_from_uuid_in_directory",
            return_value=None,
        ):
            response = self.client.get(f"/services/{service_id}")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
