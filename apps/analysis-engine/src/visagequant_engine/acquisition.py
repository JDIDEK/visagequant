from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal

ACQUISITION_SCHEMA_VERSION = "1.0.0"
ACQUISITION_PROTOCOL_VERSION = "acquisition-1.0.0"

CaptureMode = Literal["guided_video", "still_images"]
ValidationStatus = Literal["pending_calibration", "specified"]


@dataclass(frozen=True, slots=True)
class AcquisitionView:
    id: str
    label: str
    nominal_yaw_degrees: int
    yaw_tolerance_degrees: None = None
    validation_status: ValidationStatus = "pending_calibration"


@dataclass(frozen=True, slots=True)
class AcquisitionCondition:
    id: str
    instruction: str
    validation_status: ValidationStatus = "pending_calibration"


@dataclass(frozen=True, slots=True)
class AcquisitionProtocol:
    schema_version: str
    protocol_version: str
    status: Literal["draft"]
    capture_modes: tuple[CaptureMode, ...]
    ordered_views: tuple[AcquisitionView, ...]
    conditions: tuple[AcquisitionCondition, ...]
    measurements_blocked_until_complete: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


PROTOCOL = AcquisitionProtocol(
    schema_version=ACQUISITION_SCHEMA_VERSION,
    protocol_version=ACQUISITION_PROTOCOL_VERSION,
    status="draft",
    capture_modes=("guided_video", "still_images"),
    ordered_views=(
        AcquisitionView("front", "Face", 0),
        AcquisitionView("three_quarter_left", "Trois-quarts gauche", -45),
        AcquisitionView("profile_left", "Profil gauche", -90),
        AcquisitionView("three_quarter_right", "Trois-quarts droit", 45),
        AcquisitionView("profile_right", "Profil droit", 90),
    ),
    conditions=(
        AcquisitionCondition(
            "camera_position",
            "Garder la camera a hauteur des yeux et immobile pendant la sequence.",
        ),
        AcquisitionCondition(
            "distance_and_framing",
            "Garder la distance stable et le visage entierement visible sans zoom numerique.",
        ),
        AcquisitionCondition(
            "lighting",
            "Utiliser une lumiere diffuse et uniforme sans zone surexposee ni ombre dure.",
        ),
        AcquisitionCondition(
            "expression",
            "Garder une expression neutre, la bouche fermee et les yeux visibles.",
        ),
        AcquisitionCondition(
            "occlusion",
            "Degager les contours utiles du visage et retirer les objets qui les masquent.",
        ),
    ),
    measurements_blocked_until_complete=True,
)


def get_acquisition_protocol() -> AcquisitionProtocol:
    """Return the immutable acquisition protocol advertised to clients."""
    return PROTOCOL
