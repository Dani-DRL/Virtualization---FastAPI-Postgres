from fastapi import HTTPException
from typing import Any
from abc import ABC

class CustomException(HTTPException, ABC):
    status_code: int
    base_msg: str

    def __init__(self, extra: Any = None):
        msg = f"{self.base_msg}: {extra}" if extra else self.base_msg
        super().__init__(
            status_code=self.status_code, 
            detail=msg
            )

class BadRequestException(CustomException):
    status_code = 400
    base_msg = "Bad Request"

class UnauthorizedException(CustomException):
    status_code = 401
    base_msg = "Unauthorized"

class ForbiddenException(CustomException):
    status_code = 403
    base_msg = "Forbidden Access"

class NotFoundException(CustomException):
    status_code = 404
    base_msg = "Not Found"

class MethodNotAllowedException(CustomException):
    status_code = 405
    base_msg = "HTTP Method Not Allowed"

class TimeoutException(CustomException):
    status_code = 408
    base_msg = "Request Timeout"

class InternalServerErrorException(CustomException):
    status_code = 500
    base_msg = "Internal Server Error"