FROM python:3.10

WORKDIR /app

COPY . /app

ENTRYPOINT ["python", "app.py"]