FROM python:3.9-slim

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential libssl-dev libffi-dev python-dev

COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY ./app /usr/src/app
#COPY ./app /app
CMD uvicorn main:app --host 0.0.0.0
