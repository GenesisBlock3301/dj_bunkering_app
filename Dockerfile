# -----------------------------
# Stage 1: Build
# -----------------------------
FROM python:3.10.15-alpine AS builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

LABEL maintainer="Nur Amin Sifat"

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && apk add --no-cache postgresql-dev

# Copy requirements and install into a separate directory
COPY ./requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt \
    && pip install --prefix=/install --no-cache-dir --upgrade setuptools \
    && pip install --prefix=/install --no-cache-dir gunicorn

# Copy app code
COPY . .

# Collect static files
RUN mkdir -p /app/staticfiles \
    && PYTHONPATH=/install/lib/python3.10/site-packages python manage.py collectstatic --no-input -c

# Remove build dependencies
RUN apk del .build-deps

# -----------------------------
# Stage 2: Runtime
# -----------------------------
FROM python:3.10.15-alpine AS runtime

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

# Install runtime dependencies
RUN apk add --no-cache postgresql-libs

# Copy installed Python packages from build stage
COPY --from=builder /install /usr/local

# Copy app code and static files from build stage
COPY --from=builder /app /app

# Expose port
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "dj_bunkering_app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--threads", "2"]
