FROM python:3.10-alpine as base

WORKDIR /app

# Install Postgres dependencies
RUN apk update \
    && apk --no-cache --virtual .build-dependencies add postgresql-dev gcc g++ linux-headers python3-dev musl-dev jpeg-dev zlib-dev libffi-dev libwebp libwebp-tools libwebp-dev \
    && rm -rf .build-dependencies

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Install backend dependencies
RUN pip install --upgrade pip gunicorn
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add project files
COPY uploads uploads
COPY src src

ENTRYPOINT ["python", "src/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

# Prod stage
FROM base as prod

WORKDIR /app/src

CMD ["gunicorn", "taptedisker.wsgi:application", "--workers=4", "--threads=4", "--bind", "0.0.0.0:8000"]
