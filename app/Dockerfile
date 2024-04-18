FROM python:3.11.9-alpine3.19

WORKDIR /app

COPY main.py .

RUN addgroup -S app && adduser -S app -G app
USER app

CMD ["python", "main.py"]

