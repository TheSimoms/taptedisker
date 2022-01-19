FROM python:3.10-alpine as dev

WORKDIR /app

# Install Postgres dependencies
RUN apk update \
    && apk --no-cache --virtual .build-dependencies add postgresql-dev gcc python3-dev musl-dev \
    && rm -rf .build-dependencies

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Install backend dependencies
RUN pip install --upgrade pip gunicorn
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add project files
COPY src src

ENTRYPOINT ["python", "src/manage.py"]
CMD ["runserver", "0.0.0.0:8080"]

# Prod stage
FROM dev as prod

WORKDIR /app/src

CMD ["gunicorn", "taptedisker.wsgi:application", "--workers=4", "--threads=4", "--bind", "0.0.0.0:8080"]
