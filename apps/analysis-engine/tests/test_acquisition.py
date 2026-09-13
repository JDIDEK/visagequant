from __future__ import annotations

import unittest

from visagequant_engine.acquisition import (
    ACQUISITION_PROTOCOL_VERSION,
    ACQUISITION_SCHEMA_VERSION,
    get_acquisition_protocol,
)


class AcquisitionProtocolTests(unittest.TestCase):
    def test_protocol_exposes_the_complete_ordered_view_sequence(self) -> None:
        protocol = get_acquisition_protocol()

        self.assertEqual(
            tuple(view.id for view in protocol.ordered_views),
            (
                "front",
                "three_quarter_left",
                "profile_left",
                "three_quarter_right",
                "profile_right",
            ),
        )
        self.assertTrue(protocol.measurements_blocked_until_complete)

    def test_unvalidated_tolerances_are_never_invented(self) -> None:
        protocol = get_acquisition_protocol()

        self.assertEqual(protocol.status, "draft")
        self.assertTrue(all(view.yaw_tolerance_degrees is None for view in protocol.ordered_views))
        self.assertTrue(
            all(view.validation_status == "pending_calibration" for view in protocol.ordered_views)
        )
        self.assertTrue(
            all(
                condition.validation_status == "pending_calibration"
                for condition in protocol.conditions
            )
        )

    def test_serialized_protocol_is_explicitly_versioned(self) -> None:
        payload = get_acquisition_protocol().to_dict()

        self.assertEqual(payload["schema_version"], ACQUISITION_SCHEMA_VERSION)
        self.assertEqual(payload["protocol_version"], ACQUISITION_PROTOCOL_VERSION)
        self.assertEqual(payload["capture_modes"], ("guided_video", "still_images"))


if __name__ == "__main__":
    unittest.main()
