FROM mysql:5.7

COPY ./docker/db/mysql_user.sql /mnt/mysql/mysql_user.sql
COPY ./docker/db/test_database.sql /mnt/mysql/test_database.sql

WORKDIR /mnt/mysql
