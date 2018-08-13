FROM golang:1.10.3-alpine3.8
LABEL maintainer="matsub.rk@gmail.com"

COPY Gopkg.toml /go/src/app/Gopkg.toml
RUN pip install -r /tmp/requirements.txt

EXPOSE 8080
