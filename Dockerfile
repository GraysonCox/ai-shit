FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.12.1 /uv /uvx /bin/

COPY . /app

ENV UV_NO_DEV=1

WORKDIR /app
RUN uv sync --locked

CMD ["uv", "run", "discord-bot"]
