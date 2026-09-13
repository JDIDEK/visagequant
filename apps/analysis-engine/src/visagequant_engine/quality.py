from __future__ import annotations

from .domain import QualityResult, QualitySignals

QUALITY_METHOD_VERSION = "quality-0.1.0"


def assess_front_view(signals: QualitySignals) -> QualityResult:
    """Evaluate a frontal acquisition using explicit provisional gates.

    Thresholds are engineering defaults for the scaffold, not validated scientific
    cut-offs. They must be calibrated on the M1 validation dataset before release.
    """
    failures: list[str] = []

    if signals.blur_score < 0.70:
        failures.append("image_too_blurry")
    if signals.exposure_score < 0.65:
        failures.append("invalid_exposure")
    if signals.face_coverage < 0.35:
        failures.append("face_too_small")
    if abs(signals.yaw_degrees) > 8:
        failures.append("yaw_out_of_range")
    if abs(signals.pitch_degrees) > 8:
        failures.append("pitch_out_of_range")
    if abs(signals.roll_degrees) > 5:
        failures.append("roll_out_of_range")
    if signals.occlusion_score > 0.15:
        failures.append("face_occluded")
    if signals.neutral_expression_score < 0.75:
        failures.append("expression_not_neutral")

    pose_score = max(
        0.0,
        1.0
        - (
            abs(signals.yaw_degrees) / 8
            + abs(signals.pitch_degrees) / 8
            + abs(signals.roll_degrees) / 5
        )
        / 3,
    )
    score = (
        0.20 * signals.blur_score
        + 0.15 * signals.exposure_score
        + 0.10 * min(signals.face_coverage / 0.45, 1.0)
        + 0.25 * pose_score
        + 0.15 * (1.0 - signals.occlusion_score)
        + 0.15 * signals.neutral_expression_score
    )
    return QualityResult(
        accepted=not failures,
        score=round(min(max(score, 0.0), 1.0), 4),
        failures=tuple(failures),
    )
