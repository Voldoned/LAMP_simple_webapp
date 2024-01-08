from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Recesived status code is not equal to expected."
    VALIDATION_FAILED = "Validation failed"
    ANSWER_TRUE_VALUE_ERROR = "Incorrect value of the 'answer_true' field in the form!"
    HEADER_CONTENT_TYPE_NOT_JSON = "'Content-type' is not JSON."
    NOT_CREATE_TEST_QUETION_IN_DB = "The entered data was not added to the database or incorrect request data."
    NOT_DELETE_TEST_QUETION_IN_DB = "There is no record in the database for the specified ID or incorrect request data."


class HeaderContentType(Enum):
    JSON = 'application/json'
    TEXT = 'text/html'