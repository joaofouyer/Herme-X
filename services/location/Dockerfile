FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./services/location /code

RUN apt update && apt-get install -y libgeos++ && python3 -m pip install -r requirements.txt --no-cache-dir
