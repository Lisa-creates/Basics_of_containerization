FROM alpine:3.19.1

WORKDIR /db

RUN apk add sqlite && addgroup -S app && adduser -S app -G app && chown app:app .
USER app

RUN touch db.sqlite

CMD ["sqlite3", "db.sqlite"]

