from dataclasses import dataclass

# Create your views here.
from rest_framework import status as http_codes
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FieldJsonError


# La parte importante delle eccezioni e' quella di
# subclassare API exception per far intercettare gli errori
class StubError(APIException):
    status_code: int = http_codes.HTTP_400_BAD_REQUEST
    default_detail: dataclass = FieldJsonError(name='name', message='error', code='code').asdict()


class ExceptionView(APIView):
    def get(self, request, format=None):
        raise StubError()

        return Response('Prova')
