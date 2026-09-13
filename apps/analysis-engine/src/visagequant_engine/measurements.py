from __future__ import annotations

from collections.abc import Callable, Mapping

from .domain import Measurement, Point2D
from .geometry import GeometryError, canthal_tilt_degrees, combined_confidence, distance, safe_ratio

MEASUREMENT_METHOD_VERSION = "morphometry-0.1.0"
Landmarks = Mapping[str, Point2D]


def _measurement(
    key: str,
    label: str,
    unit: str,
    required: tuple[str, ...],
    landmarks: Landmarks,
    compute: Callable[[Landmarks], float],
) -> Measurement:
    missing = tuple(name for name in required if name not in landmarks)
    if missing:
        return Measurement(
            key=key,
            label=label,
            value=None,
            unit=unit,  # type: ignore[arg-type]
            confidence=0.0,
            method_version=MEASUREMENT_METHOD_VERSION,
            unavailable_reason=f"missing_landmarks:{','.join(missing)}",
        )

    points = tuple(landmarks[name] for name in required)
    try:
        value = compute(landmarks)
    except GeometryError as error:
        return Measurement(
            key=key,
            label=label,
            value=None,
            unit=unit,  # type: ignore[arg-type]
            confidence=0.0,
            method_version=MEASUREMENT_METHOD_VERSION,
            unavailable_reason=str(error),
        )

    return Measurement(
        key=key,
        label=label,
        value=round(value, 4),
        unit=unit,  # type: ignore[arg-type]
        confidence=round(combined_confidence(*points), 4),
        method_version=MEASUREMENT_METHOD_VERSION,
    )


def compute_measurements(landmarks: Landmarks) -> tuple[Measurement, ...]:
    """Compute a deliberately small, auditable set of 2D baseline metrics."""
    definitions = (
        (
            "left_canthal_tilt",
            "Left canthal tilt",
            "degrees",
            ("left_eye_inner", "left_eye_outer"),
            lambda p: canthal_tilt_degrees(p["left_eye_inner"], p["left_eye_outer"]),
        ),
        (
            "right_canthal_tilt",
            "Right canthal tilt",
            "degrees",
            ("right_eye_inner", "right_eye_outer"),
            lambda p: canthal_tilt_degrees(p["right_eye_inner"], p["right_eye_outer"]),
        ),
        (
            "intercanthal_to_face_width",
            "Intercanthal distance / face width",
            "ratio",
            ("left_eye_inner", "right_eye_inner", "face_left", "face_right"),
            lambda p: safe_ratio(
                distance(p["left_eye_inner"], p["right_eye_inner"]),
                distance(p["face_left"], p["face_right"]),
            ),
        ),
        (
            "facial_width_to_height",
            "Facial width / height",
            "ratio",
            ("face_left", "face_right", "hairline_mid", "chin_mid"),
            lambda p: safe_ratio(
                distance(p["face_left"], p["face_right"]),
                distance(p["hairline_mid"], p["chin_mid"]),
            ),
        ),
    )
    return tuple(
        _measurement(key, label, unit, required, landmarks, compute)
        for key, label, unit, required, compute in definitions
    )
