FROM nginx:1.11.13-alpine
MAINTAINER Den Elston "4665284@gmail.com"

# ..
ADD ./src /carcasspg
RUN rm /etc/nginx/conf.d/default.conf \
    && ln -s /carcasspg/deploy/nginx.conf /etc/nginx/conf.d/carcasspg.conf
