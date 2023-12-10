FROM python:3.12-alpine

WORKDIR ./api-tests

VOLUME /allure-results

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN apk update && apk upgrade && apk add bash

COPY . .

CMD pytest ./tests/test* --alluredir=allure-results
