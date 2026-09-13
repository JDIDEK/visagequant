from __future__ import annotations

from math import atan2, degrees, hypot

from .domain import Point2D


class GeometryError(ValueError):
    """Raised when a geometric quantity cannot be computed safely."""


def distance(a: Point2D, b: Point2D) -> float:
    return hypot(b.x - a.x, b.y - a.y)


def safe_ratio(numerator: float, denominator: float) -> float:
    if abs(denominator) < 1e-12:
        raise GeometryError("ratio denominator is zero")
    return numerator / denominator


def line_angle_degrees(a: Point2D, b: Point2D) -> float:
    """Return the signed image-plane angle from a to b in degrees."""
    if a.x == b.x and a.y == b.y:
        raise GeometryError("an angle requires two distinct points")
    return degrees(atan2(-(b.y - a.y), b.x - a.x))


def canthal_tilt_degrees(inner: Point2D, outer: Point2D) -> float:
    """Return canthal tilt, positive when the outer canthus is higher.

    Image coordinates grow downwards. Using the absolute horizontal span makes
    the convention identical for the left and right eye.
    """
    horizontal_span = abs(outer.x - inner.x)
    if horizontal_span < 1e-12:
        raise GeometryError("canthal tilt requires a non-zero horizontal span")
    return degrees(atan2(inner.y - outer.y, horizontal_span))


def midpoint(a: Point2D, b: Point2D) -> Point2D:
    return Point2D(
        x=(a.x + b.x) / 2,
        y=(a.y + b.y) / 2,
        confidence=min(a.confidence, b.confidence),
    )


def combined_confidence(*points: Point2D) -> float:
    if not points:
        raise GeometryError("at least one point is required")
    return min(min(max(point.confidence, 0.0), 1.0) for point in points)
