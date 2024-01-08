from requests import Response

from src.enums.global_enums import GlobalErrorMessages as GEM, \
    HeaderContentType as HCP


class BaseResponse:

    def __init__(self, response: Response):
        self.response = response
        self.response_status_code = response.status_code
        self.response_headers = dict(response.headers)
        self.request_method = response.request.method
        self.request_headers = dict(response.request.headers)

        if self.response_headers['Content-Type'] == HCP.JSON.value:
            self.responce_json = response.json()
        else:
            self.responce_json = None

    def __str__(self):
        output = f"\nStatus code: {self.response_status_code}" \
                 f" Request URL: {self.response.url}"

        if self.responce_json:
            return output + f" Request JSON: {self.responce_json}"
        else:
            return output

    def get_request_headers(self) -> dict:
        return self.request_headers

    def get_response_headers(self) -> dict:
        return self.response_headers

    def assert_status_code(self, status_code):
        if isinstance(status_code, (list, tuple)):
            assert self.response_status_code in status_code, \
                GEM.WRONG_STATUS_CODE.value
        else:
            assert self.response_status_code == status_code, \
                GEM.WRONG_STATUS_CODE.value + f" Status code: {self.response_status_code}"

    def assert_has_response_json(self):
        assert self.response_headers['Content-Type'] == HCP.JSON.value, \
            GEM.HEADER_CONTENT_TYPE_NOT_JSON.value + \
            f" Header 'Content-type': {self.response_headers['Content-Type']}."

        assert self.responce_json, f"JSON: {self.response_json}."

    def validate_json(self, schema):
        if self.responce_json:
            if isinstance(self.responce_json, (list, tuple)):
                for i in self.responce_json:
                    schema.parse_obj(i)
            else:
                schema.parse_obj(self.responce_json)

            return self.responce_json
        else:
            return None
