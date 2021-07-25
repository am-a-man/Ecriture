
FROM python:3.9.5-alpine

ENV PYTHONUNBUFFERED 1
COPY . .
RUN pip3 install -r /server/requirements.txt


FROM node:14-alpine
COPY --from=0 /  .
WORKDIR /server/api_outlet
COPY package*.json ./
RUN npm install
WORKDIR / 

WORKDIR /client
COPY package*.json ./
RUN npm install

WORKDIR / 


