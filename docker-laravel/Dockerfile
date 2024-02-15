# FROM php:8.3.2-fpm-alpine3.19
FROM php:7.2-fpm-alpine
WORKDIR /var/www/html
# Install PHP Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
COPY . .

# Sao không thấy CMD đâu? vào hẳn gốc rễ của image 8.3.2-fpm-alpine3.19 và kéo xuống cuối cùng:
# https://github.com/docker-library/php/blob/master/8.1/alpine3.19/fpm/Dockerfile
# Ta sẽ thấy 2 dòng:
# EXPOSE 9000
# CMD ["php-fpm"]

# https://viblo.asia/p/dockerize-ung-dung-laravel-vyDZOao75wj