FROM python:3.7-alpine
MAINTAINER talented(https://github.com/talented)

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
COPY docker-entrypoint-api.sh /app/docker-entrypoint-api.sh
RUN chmod +x /app/docker-entrypoint-api.sh

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip3 install -r ./requirements.txt
RUN apk del .tmp-build-deps



WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
