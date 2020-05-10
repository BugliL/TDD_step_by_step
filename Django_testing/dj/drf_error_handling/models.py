import dataclasses
import json
from dataclasses import dataclass
from typing import List

from rest_framework import status
from rest_framework.exceptions import APIException


@dataclass(frozen=True)
class JsonError:
    """
    Classe base per la gestione degli errori
    """

    code: str
    message: str

    def __str__(self) -> str:
        return json.dumps(self.asdict())

    def asdict(self) -> dict:
        return dataclasses.asdict(self)


@dataclass(frozen=True)
class FieldJsonError(JsonError):
    """
    Classe per la gestione degli errori relativi ai campi delle entita'
    """

    name: str

    def asdict(self) -> dict:
        return {
            self.name: {
                'code': self.code,
                'message': self.message
            }
        }


class FieldJsonErrorList:
    """
    Classe Collection di FieldJsonError
    """
    global_error: JsonError = FieldJsonError(name='global', code='', message='')
    error_list: List[JsonError] = []
    has_error: bool = False

    @classmethod
    def add(cls, name: str, message: str, code: str) -> None:
        cls.error_list.append(FieldJsonError(name=name, message=message, code=code))
        cls.has_error = True

    @classmethod
    def set_global_error(cls, message: str, code: str) -> None:
        cls.global_error = JsonError(message=message, code=code)
        cls.has_error = True

    @classmethod
    def asdict(cls) -> dict:
        result = {**cls.global_error.asdict()}
        [result.update(d.asdict()) for d in cls.error_list]
        return result

    @classmethod
    def reset(cls):
        cls.global_error = FieldJsonError(name='global', code='', message='')
        cls.error_list = []
        cls.has_error = False

    @classmethod
    def raise_error(cls) -> None:
        class Error(APIException):
            status_code: int = status.HTTP_400_BAD_REQUEST
            default_detail: dataclass = cls.asdict()

        if cls.has_error:
            raise Error()
