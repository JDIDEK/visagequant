FROM python:3.12-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/opt/visagequant-venv \
    PATH="/opt/visagequant-venv/bin:$PATH"

WORKDIR /app

RUN groupadd --system visagequant \
    && useradd --system --gid visagequant --create-home visagequant

COPY pyproject.toml uv.lock ./
COPY src ./src
COPY tests ./tests

RUN python -m pip install "uv==0.12.13" \
    && uv sync --frozen --no-dev --no-editable

USER visagequant

EXPOSE 8765

CMD ["python", "-m", "uvicorn", "visagequant_engine.api:app", "--host", "0.0.0.0", "--port", "8765"]
