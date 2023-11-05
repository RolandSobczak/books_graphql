FROM python:3.12

WORKDIR /src

COPY poetry.lock pyproject.toml /src/

RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root

COPY . .

CMD uvicorn backend.main:app --reload --host 0.0.0.0