FROM python:3.11.7-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

    
RUN pip install --upgrade pip

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt

COPY src src
COPY modules modules
COPY api api


EXPOSE 8086