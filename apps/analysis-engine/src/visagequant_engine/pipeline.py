from __future__ import annotations

from typing import Any

from .domain import AnalysisResult, Point2D, QualitySignals
from .measurements import compute_measurements
from .quality import QUALITY_METHOD_VERSION, assess_front_view

PIPELINE_VERSION = "0.1.0"
SCHEMA_VERSION = "1.0.0"


def analyze_front_view(payload: dict[str, Any]) -> AnalysisResult:
    signals = QualitySignals(**payload["quality_signals"])
    quality = assess_front_view(signals)
    provenance = {
        "quality_method_version": QUALITY_METHOD_VERSION,
        "source": payload.get("source", "unknown"),
        "calibrated_scale": False,
        "notice": "Baseline 2D scaffold; not a validated clinical or aesthetic analysis.",
    }

    if not quality.accepted:
        return AnalysisResult(
            schema_version=SCHEMA_VERSION,
            pipeline_version=PIPELINE_VERSION,
            status="rejected",
            quality=quality,
            provenance=provenance,
        )

    landmarks = {
        name: Point2D(**coordinates) for name, coordinates in payload.get("landmarks", {}).items()
    }
    return AnalysisResult(
        schema_version=SCHEMA_VERSION,
        pipeline_version=PIPELINE_VERSION,
        status="completed",
        quality=quality,
        measurements=compute_measurements(landmarks),
        provenance=provenance,
    )
