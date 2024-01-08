import time
import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ROOT_USER: str
    ROOT_PASSWORD: str
    LARAVEL_USER: str
    LARAVEL_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


os.system("sudo docker-compose build")
os.system("sudo docker-compose up -d mysql")

time.sleep(60*2)

ROOT_USER = settings.ROOT_USER
ROOT_PASSWORD = settings.ROOT_PASSWORD

LARAVEL_USER = settings.LARAVEL_USER
LARAVEL_PASSWORD = settings.LARAVEL_PASSWORD

COMMAND_FOR_DB_CONTAINER = f"'exec mysqldump -u{ROOT_USER} -p{ROOT_PASSWORD} mysql user < mysql_user.sql && exec mysqldump -u{LARAVEL_USER} -p{LARAVEL_PASSWORD} test_database < test_database.sql'"
COMMAND_FOR_APP_CONTAINER = f"'cd /var/www/mylarapp && php artisan migrate && php artisan db:seed'"

os.system(f"sudo docker exec -i db sh -c {COMMAND_FOR_DB_CONTAINER}")

os.system("sudo docker-compose up -d app ")
os.system(f"sudo docker exec -i app sh -c {COMMAND_FOR_APP_CONTAINER}")

os.system("sudo docker-compose up tests_python")
os.system("sudo docker-compose up tests_locust")