ARG PYTHON_IMAGE=python:3.12.3

FROM ${PYTHON_IMAGE}

WORKDIR /app

COPY ./backend ./backend
COPY ./alembic.ini ./
COPY ./poetry.lock ./
COPY ./pyproject.toml ./
COPY ./static ./static

ENV VENV_PATH="/opt/venv"

RUN python -m venv ${VENV_PATH}
ENV PATH="$VENV_PATH/bin:$PATH"

SHELL [ "/bin/bash", "-c"]

RUN source "${VENV_PATH}/bin/activate" && pip install poetry
RUN source "${VENV_PATH}/bin/activate" && poetry config virtualenvs.create false
RUN source "${VENV_PATH}/bin/activate" && poetry install --no-root
