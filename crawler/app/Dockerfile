
FROM python:3.9.5-alpine

ENV PYTHONUNBUFFERED 1
COPY /requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
RUN pip3 list

RUN mkdir /app
COPY ./app /app
#WORKDIR /app




FROM node:14-alpine
COPY --from=0 /  .

RUN mkdir /api_outlet
COPY ./api_outlet /api_outlet
WORKDIR /api_outlet
RUN pwd
COPY package*.json ./
RUN npm install

WORKDIR / 


