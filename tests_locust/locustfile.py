from locust import HttpUser, task, constant_throughput
from pydantic import ValidationError

from src.base_classes.base_response import BaseResponse
from src.pydantic_schema import QuetionSchema
from src.enums.global_enums import GlobalErrorMessages as GEM

HEADERS = {
    'Accept': 'text/html,'
              'application/json,'
              'application/xhtml+xml,'
              'application/xml;q=0.9,'
              'image/avif,'
              'image/webp,'
              'image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'localhost:8000',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", '
                 '"Chromium";v="114", '
                 '"Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/114.0.0.0 '
                  'Safari/537.36'
}

DATA_FOR_CREATE_QUETION = {
    'quetion': 'Где?',
    'answer1': 'Здесь',
    'answer2': 'Там',
    'answer3': 'Нигде',
    'answer4': 'Тут',
    'answer_true': 'answer1'
}


class TestLocust(HttpUser):
    # Означает, что пользователь будет отправлять 1 запрос в секунду
    wait_time = constant_throughput(0.5)

    @task(1)
    def get_test_request(self):
        transaction = self.get_test_request.__name__

        with self.client.get(
                '/test',
                headers=HEADERS,
                catch_response=True,
                name=transaction
        ) as response2:
            try:
                BaseResponse(response2).assert_status_code(200)
            except Exception as e:
                response2.failure(e)

    @task(1)
    def get_create_test_request(self):
        transaction = self.get_create_test_request.__name__

        # Создаем экземпляр класса BaseResponse и проверяем корректность
        # ответа сервера
        with self.client.post(
                '/api/test/create/post',
                headers=HEADERS,
                data=DATA_FOR_CREATE_QUETION,
                catch_response=True,
                name=transaction
        ) as response_create:

            try:
                response_create_test_obj = BaseResponse(response_create)
                response_create_test_obj.assert_status_code(200)
                response_create_test_obj.assert_has_response_json()
                response_create_test_obj.validate_json(QuetionSchema)
            except Exception as e:
                response_create.failure(e)

        # Проверяем создалась ли запись в базе данных по нашему запросу,
        # используя API
        with self.client.get(
                '/api/tests',
                headers=HEADERS,
                catch_response=True,
                name=transaction
        ) as response_get_tests:
            try:
                response_get_tests_obj = BaseResponse(response_get_tests)
                assert response_create_test_obj.responce_json \
                       in response_get_tests_obj.responce_json, \
                    GEM.NOT_CREATE_TEST_QUETION_IN_DB.value
            except Exception as e:
                response_create.failure(e)

        # Удаляем созданную ранее запись в таблице в базе данных,
        # используя значение id и API
        try:
            response_create_test_id = response_create_test_obj.responce_json['id']
            self.client.post(
                '/api/test/delete/post',
                headers=HEADERS,
                data={
                    'id_quetion': str(response_create_test_id)
                },
                catch_response=True,
                name=transaction
            )
        except Exception as e:
            response_create.failure(e)

        # Проверяем, что запись из таблицы была удалена, используя API
        with self.client.get(
                '/api/tests',
                headers=HEADERS,
                catch_response=True,
                name=transaction
        ) as response_last:
            try:
                response_last_obj = BaseResponse(response_last)
                assert response_create_test_obj.responce_json \
                       not in response_last_obj.responce_json, \
                    GEM.NOT_DELETE_TEST_QUETION_IN_DB.value
            except Exception as e:
                response_last.failure(e)

    @task(1)
    def get_tests_api_request(self):
        transaction = self.get_tests_api_request.__name__
        with self.client.get(
                '/api/tests',
                headers=HEADERS,
                catch_response=True,
                name=transaction
        ) as response:
            try:
                resp_obj = BaseResponse(response)
                resp_obj.assert_status_code(200)
                resp_obj.assert_has_response_json()
                resp_obj.validate_json(QuetionSchema)
            except Exception as e:
                response.failure(e)
