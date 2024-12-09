FROM python:3.10.15-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

LABEL maintainer="Nur Amin Sifat"

WORKDIR /app

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev \
    && apk add --no-cache postgresql-libs

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade setuptools \
    && pip install --no-cache-dir gunicorn

COPY . .

RUN mkdir -p /app/staticfiles \
    && python manage.py collectstatic --no-input -c

RUN apk del .build-deps

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
