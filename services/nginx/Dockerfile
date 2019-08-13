FROM nginx:1.15.12-alpine
ADD ./services/nginx/vhost.conf /etc/nginx/conf.d/default.conf


RUN mkdir /etc/nginx/ssl
ADD ./services/nginx/nginx.crt /etc/nginx/ssl
ADD ./services/nginx/nginx.key /etc/nginx/ssl