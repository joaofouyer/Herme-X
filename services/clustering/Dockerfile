FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./services/clustering /code

RUN apt update
RUN apt install make automake gcc g++ subversion python3-dev

RUN python3 -m pip install -r requirements.txt --no-cache-dir