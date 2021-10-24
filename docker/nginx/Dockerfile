FROM nginx:1.18
ADD docker/nginx/app.conf /etc/nginx/conf.d/default.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
WORKDIR /var/www
EXPOSE 80