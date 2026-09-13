from __future__ import annotations

import unittest

from visagequant_engine.pipeline import analyze_front_view


def valid_payload() -> dict[str, object]:
    return {
        "source": "synthetic-test",
        "quality_signals": {
            "blur_score": 0.94,
            "exposure_score": 0.91,
            "face_coverage": 0.44,
            "yaw_degrees": 1.2,
            "pitch_degrees": -0.8,
            "roll_degrees": 0.5,
            "occlusion_score": 0.02,
            "neutral_expression_score": 0.96,
        },
        "landmarks": {
            "face_left": {"x": 100, "y": 250, "confidence": 0.98},
            "face_right": {"x": 500, "y": 250, "confidence": 0.98},
            "hairline_mid": {"x": 300, "y": 50, "confidence": 0.92},
            "chin_mid": {"x": 300, "y": 650, "confidence": 0.97},
            "left_eye_inner": {"x": 250, "y": 250, "confidence": 0.99},
            "left_eye_outer": {"x": 180, "y": 242, "confidence": 0.98},
            "right_eye_inner": {"x": 350, "y": 250, "confidence": 0.99},
            "right_eye_outer": {"x": 420, "y": 242, "confidence": 0.98},
        },
    }


class PipelineTests(unittest.TestCase):
    def test_valid_acquisition_completes(self) -> None:
        result = analyze_front_view(valid_payload())
        self.assertEqual(result.status, "completed")
        self.assertTrue(result.quality.accepted)
        self.assertEqual(len(result.measurements), 4)

    def test_invalid_acquisition_is_rejected_before_measurements(self) -> None:
        payload = valid_payload()
        quality = payload["quality_signals"]
        assert isinstance(quality, dict)
        quality["blur_score"] = 0.2

        result = analyze_front_view(payload)

        self.assertEqual(result.status, "rejected")
        self.assertIn("image_too_blurry", result.quality.failures)
        self.assertEqual(result.measurements, ())

    def test_missing_landmark_does_not_invent_value(self) -> None:
        payload = valid_payload()
        landmarks = payload["landmarks"]
        assert isinstance(landmarks, dict)
        del landmarks["hairline_mid"]

        result = analyze_front_view(payload)
        measure = next(m for m in result.measurements if m.key == "facial_width_to_height")

        self.assertIsNone(measure.value)
        self.assertEqual(measure.confidence, 0)
        self.assertIn("hairline_mid", measure.unavailable_reason or "")


if __name__ == "__main__":
    unittest.main()
