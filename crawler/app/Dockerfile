
FROM python:3.9.5-alpine

ENV PYTHONUNBUFFERED 1
COPY /requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
RUN pip3 list

RUN mkdir /app
COPY ./app /app
WORKDIR /app




