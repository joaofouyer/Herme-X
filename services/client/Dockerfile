FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code && mkdir /code/datasets
WORKDIR /code
ADD ./services/client /code


RUN \
 apk update \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir
# apk --purge del .build-deps \
RUN apk add nodejs
RUN apk add npm
RUN npm install -g yarn

ADD ./services/datasets /code/datasets

