FROM python:3.11 AS builder

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --default-timeout=1000 --no-cache-dir -r requirements.txt


FROM python:3.11-slim

WORKDIR /usr/src/app

RUN useradd -m app

COPY --from=builder /usr/local /usr/local


ENV PATH=/usr/local/bin:$PATH

COPY --chown=app:app . .

USER app

CMD [ "python", "-m", "app" ]