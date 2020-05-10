import dataclasses
import json
from collections import defaultdict
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
    error: str

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
    classe: str

    def asdict(self) -> dict:
        return {
            self.classe: {
                self.name: {'code': self.code, 'error': self.error}
            }
        }


class FieldJsonErrorList:
    """
    Classe Collection di FieldJsonError
    """
    global_error = JsonError(error='', code='')
    error_list: List[JsonError] = []
    has_error: bool = False

    @classmethod
    def reset(cls):
        cls.global_error = JsonError(code='', error='')
        cls.error_list = []
        cls.has_error = False

    @classmethod
    def add(cls, classe: str, name: str, error: str, code: str) -> None:
        cls.error_list.append(FieldJsonError(classe=classe, name=name, error=error, code=code))
        cls.has_error = True

    @classmethod
    def set_global_error(cls, error: str, code: str) -> None:
        cls.global_error = JsonError(error=error, code=code)
        cls.has_error = True

    @classmethod
    def asdict(cls) -> dict:
        result = defaultdict(lambda: defaultdict(dict))
        result['global'] = cls.global_error.asdict()
        for d in cls.error_list:  # type: FieldJsonError
            result[d.classe][d.name] = {'code': d.code, 'error': d.error}

        return result

    @classmethod
    def raise_error(cls) -> None:
        class Error(APIException):
            status_code: int = status.HTTP_400_BAD_REQUEST
            default_detail: dataclass = cls.asdict()

        if cls.has_error:
            raise Error()


ERROR_MANAGER = FieldJsonError
