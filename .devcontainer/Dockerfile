# based on https://github.com/devcontainers/templates/tree/main/src/python

FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

RUN python -m pip install pip --upgrade \
    && python -m pip install poetry \
    && poetry config virtualenvs.in-project true

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends default-mysql-client
