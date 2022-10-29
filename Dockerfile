FROM python:3.11
LABEL maintainer="Thomas Lazarus (Github: lazarust)"

ENV \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    # Set the Django settings module for testing \
    DJANGO_SETTINGS_MODULE=config.settings.base \
    USER=root \
    # This keeps Python from buffering stdin/stdout \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/code

WORKDIR /code

RUN set -ex && \
    pip install -U setuptools wheel pip  && \
    cp /etc/skel/.bashrc /root/.bashrc

COPY requirements.txt ./

## Install Python Packages
RUN --mount=type=cache,target=/root/.cache/pip pip install -r /code/requirements.txt