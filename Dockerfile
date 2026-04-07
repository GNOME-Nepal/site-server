# Specify the platform as an argument
ARG PLATFORM=linux/amd64

# Base image with specified platform
FROM --platform=$PLATFORM python:3.11-slim AS base


# Create a non-root user and group
RUN groupadd -r gnome_group && useradd -r -g gnome_group -d /app -s /bin/bash gnome_user

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    pkg-config build-essential libpq-dev ca-certificates  \
    && pip install --no-cache-dir --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --no-compile -r requirements.txt
COPY . .

RUN chmod +x Makefile
# make empty directory for logs and media
RUN mkdir logs media
RUN chown -R gnome_user:gnome_group /app
USER gnome_user

FROM base AS worker


FROM base AS development
EXPOSE 8000
CMD ["make", "dev"]

FROM base AS production
EXPOSE 8000
CMD ["make", "prod"]
