FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./services/location /code


RUN \
 python3 -m pip install -r requirements.txt --no-cache-dir