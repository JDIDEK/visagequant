from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal


@dataclass(frozen=True, slots=True)
class Point2D:
    x: float
    y: float
    confidence: float = 1.0


@dataclass(frozen=True, slots=True)
class QualitySignals:
    blur_score: float
    exposure_score: float
    face_coverage: float
    yaw_degrees: float
    pitch_degrees: float
    roll_degrees: float
    occlusion_score: float
    neutral_expression_score: float


@dataclass(frozen=True, slots=True)
class QualityResult:
    accepted: bool
    score: float
    failures: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Measurement:
    key: str
    label: str
    value: float | None
    unit: Literal["ratio", "degrees", "percent", "millimeters"]
    confidence: float
    method_version: str
    unavailable_reason: str | None = None


@dataclass(frozen=True, slots=True)
class AnalysisResult:
    schema_version: str
    pipeline_version: str
    status: Literal["completed", "rejected"]
    quality: QualityResult
    measurements: tuple[Measurement, ...] = ()
    provenance: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
