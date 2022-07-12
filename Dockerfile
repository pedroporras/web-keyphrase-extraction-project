FROM public.ecr.aws/docker/library/python:3.8-slim

COPY app /app/app
COPY requirements.txt /app/requirements.txt
WORKDIR /app/

RUN apt update
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000