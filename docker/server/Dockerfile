FROM yumechang/apache24_php82

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
COPY ./larapp /var/www/mylarapp
COPY ./docker/server/larapp.conf /etc/apache2/sites-available/000-default.conf

WORKDIR /var/www/mylarapp
RUN composer install && service apache2 restart

EXPOSE 80
CMD apachectl -D FOREGROUND

