FROM python:3.6-slim

LABEL \
Name=proxied \
Version=X0.1

ENV PYTHONUNBUFFERED=1
ENV PYTHONBREAKPOINT=0

COPY ./requirements.txt /app/dev/

WORKDIR /app/dev

RUN  pip install -r requirements.txt

COPY ./dev /app/dev

COPY ./tools/tinyproxy/filter /app/tools/tinyproxy/filter

ENTRYPOINT [ "gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app", "--log-level=info", "--access-logfile=-", "--error-logfile=-"]

EXPOSE 5000
