from __future__ import annotations

import unittest

from visagequant_engine.domain import Point2D
from visagequant_engine.geometry import (
    GeometryError,
    canthal_tilt_degrees,
    distance,
    line_angle_degrees,
    safe_ratio,
)


class GeometryTests(unittest.TestCase):
    def test_distance(self) -> None:
        self.assertEqual(distance(Point2D(0, 0), Point2D(3, 4)), 5)

    def test_horizontal_angle(self) -> None:
        self.assertEqual(line_angle_degrees(Point2D(0, 0), Point2D(2, 0)), 0)

    def test_positive_image_plane_tilt(self) -> None:
        self.assertAlmostEqual(line_angle_degrees(Point2D(0, 1), Point2D(1, 0)), 45)

    def test_canthal_tilt_is_side_independent(self) -> None:
        left = canthal_tilt_degrees(Point2D(250, 250), Point2D(180, 242))
        right = canthal_tilt_degrees(Point2D(350, 250), Point2D(420, 242))
        self.assertAlmostEqual(left, right)
        self.assertAlmostEqual(left, 6.5198, places=4)

    def test_zero_denominator_is_explicit(self) -> None:
        with self.assertRaises(GeometryError):
            safe_ratio(1, 0)


if __name__ == "__main__":
    unittest.main()
