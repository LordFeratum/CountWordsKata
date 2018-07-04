FROM python:3.6-alpine3.4

RUN apk --no-cache add \
      ca-certificates \
      openssl-dev \
      libffi-dev \
      libc-dev 

ENV PYTHONPATH=/app/src/
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

CMD ["python", "src/word_count.py"]
