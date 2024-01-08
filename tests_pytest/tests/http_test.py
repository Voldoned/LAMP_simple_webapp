import pytest

from src.base_classes.base_response import BaseResponse
from src.base_classes.api_client import APIClient


class TestHTTP:
    URLS_FOR_GET_REQUESTS = [
        '/',
        '/test',
        '/test/create',
        '/test/delete',
        '/api/tests',
    ]

    @pytest.mark.parametrize('url_path', URLS_FOR_GET_REQUESTS)
    def test_status_code_get_request(self, domen, headers_for_requests, url_path):
        response = APIClient(domen).get(
            path=url_path,
            headers=headers_for_requests
        )
        BaseResponse(response).assert_status_code(200)

    @pytest.mark.skip('Возникает ошибка 419 из-за того, '
                      'что этот POST-запрос не к API')
    def test_status_code_post_request(self, domen, session, headers_for_requests):
        site = APIClient(domen, session)

        response1 = site.get(
            path='/test/create',
            headers=headers_for_requests
        )

        response = site.post(
            path='/test/create/post',
            headers=response1.headers,
            data={
                'quetion': 'Где?',
                'answer1': 'Здесь',
                'answer2': 'Там',
                'answer3': 'Нигде',
                'answer4': 'Тут',
                'answer_true': 'answer1'
            }
        )
        # print(BaseResponse(response).response_status_code)
        BaseResponse(response).assert_status_code(200)

