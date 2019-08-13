FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./services/clustering /code

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN \
 python3 -m pip install -r requirements.txt --no-cache-dir