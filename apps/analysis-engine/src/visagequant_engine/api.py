from __future__ import annotations

import os
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .acquisition import get_acquisition_protocol
from .pipeline import analyze_front_view

app = FastAPI(title="VisageQuant local engine", version="0.1.0")

allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "VISAGEQUANT_ALLOWED_ORIGINS",
        "http://127.0.0.1:1420,http://localhost:1420",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/acquisition-protocol")
def acquisition_protocol() -> dict[str, Any]:
    return get_acquisition_protocol().to_dict()


@app.post("/v1/analyses/front")
def analyze(payload: dict[str, Any]) -> dict[str, Any]:
    return analyze_front_view(payload).to_dict()
