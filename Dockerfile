FROM python:3.6-alpine3.4

ARG reqs=base

RUN apk --no-cache add \
      ca-certificates \
      openssl-dev \
      libffi-dev \
      libc-dev 

ENV PYTHONPATH=/app/src/
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements /app/requirements
RUN pip install -r /app/requirements/${reqs}.txt

COPY . /app

COPY docker/entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]

CMD ["run"]
