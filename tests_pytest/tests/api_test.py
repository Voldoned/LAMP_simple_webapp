import pytest
from requests import Response

from src.base_classes.base_response import BaseResponse
from src.base_classes.api_client import APIClient
from src.pydantic_schema import QuetionSchema
from src.enums.global_enums import GlobalErrorMessages as GEM


class TestAPI:
    DATA_FOR_CREATE_TEST_QUETION = [
        {
            'quetion': 'Где?',
            'answer1': 'Здесь',
            'answer2': 'Там',
            'answer3': 'Нигде',
            'answer4': 'Тут',
            'answer_true': 'answer1'
        }
    ]

    def _testing_response(self, response: Response):
        response_obj = BaseResponse(response)
        response_obj.assert_status_code(200)
        response_obj.assert_has_response_json()
        response_obj.validate_json(QuetionSchema)

    def test_api_get_quetions(self, domen: str, headers_for_requests: dict):
        response = APIClient(domen).get(
            path='/api/tests',
            headers=headers_for_requests
        )

        response_obj = BaseResponse(response)
        response_obj.assert_status_code(200)
        response_obj.assert_has_response_json()
        response_obj.validate_json(QuetionSchema)

    @pytest.mark.parametrize('data_test_quetion', DATA_FOR_CREATE_TEST_QUETION)
    def test_api_post_create_and_delete_quetion(self, domen: str,
                                                headers_for_requests: dict,
                                                data_test_quetion: dict):
        # Создаем объект клиента для запросов на конкретный домен
        site = APIClient(domen)

        # Отправляем POST-запрос с заполненной формой для создания записи
        # в таблице в базе данных
        response_create_test = site.post(
            path='/api/test/create/post',
            headers=headers_for_requests,
            data=data_test_quetion
        )

        # Создаем экземпляр класса BaseResponse и проверяем корректность
        # ответа сервера
        response_create_test_obj = BaseResponse(response_create_test)
        response_create_test_obj.assert_status_code(200)
        response_create_test_obj.assert_has_response_json()
        response_create_test_obj.validate_json(QuetionSchema)

        # Проверяем создалась ли запись в базе данных по нашему запросу,
        # используя API
        response_get_tests = site.get(
            path='/api/tests',
            headers=headers_for_requests
        )
        response_get_tests_obj = BaseResponse(response_get_tests)
        assert response_create_test_obj.responce_json \
               in response_get_tests_obj.responce_json, \
            GEM.NOT_CREATE_TEST_QUETION_IN_DB.value

        # Удаляем созданную ранее запись в таблице в базе данных,
        # используя значение id и API
        response_create_test_id = response_create_test_obj.responce_json['id']
        site.post(
            path='/api/test/delete/post',
            headers=headers_for_requests,
            data={
                'id_quetion': str(response_create_test_id)
            }
        )

        # Проверяем, что запись из таблицы была удалена, используя API
        response_last = site.get(
            path='/api/tests',
            headers=headers_for_requests
        )
        response_last_obj = BaseResponse(response_last)
        assert response_create_test_obj.responce_json \
               not in response_last_obj.responce_json, \
            GEM.NOT_DELETE_TEST_QUETION_IN_DB.value
