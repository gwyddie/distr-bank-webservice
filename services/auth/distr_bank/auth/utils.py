from http import HTTPStatus
from typing import Union

from distr_bank.auth.typing import Response


def create_error(message: str, status_code: Union[HTTPStatus, int]) -> Response:
    """
    Creates an error response

    Args:
        message (str): message of the error
        status_code (Union[HTTPStatus, int]): HTTP status of the error

    Returns:
        Response: error response
    """
    body = {
        "status_code": status_code,
        "message": message,
    }
    return body, status_code
