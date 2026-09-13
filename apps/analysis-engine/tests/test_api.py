from __future__ import annotations

import json
import unittest

from visagequant_engine.api import acquisition_protocol, app


class ApiTests(unittest.TestCase):
    def test_acquisition_protocol_endpoint_returns_json_contract(self) -> None:
        routes = {route.path for route in app.routes}
        payload = json.loads(json.dumps(acquisition_protocol()))

        self.assertIn("/v1/acquisition-protocol", routes)
        self.assertEqual(payload["schema_version"], "1.0.0")
        self.assertEqual(payload["protocol_version"], "acquisition-1.0.0")
        self.assertEqual(len(payload["ordered_views"]), 5)
        self.assertIsInstance(payload["ordered_views"], list)
        self.assertTrue(payload["measurements_blocked_until_complete"])


if __name__ == "__main__":
    unittest.main()
