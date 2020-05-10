from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ErrorHandlingApiTest(APITestCase):
    def test_base_call(self):
        response = self.client.get('/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_field_error(self):
        url = reverse('drf_error_handling:index')
        data = {'name': {'code': 'code', 'error': 'error'}}
        response = self.client.get(url)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertDictEqual(data, response.data)
