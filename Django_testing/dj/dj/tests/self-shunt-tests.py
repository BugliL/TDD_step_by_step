from django.http import HttpRequest
from django.test import TestCase
from .. import views

"""
Self-shunt
How do you test that one object communicates correctly with another?
Have the object under test communicate with the test case instead of with the object is expects


This patter is applied to a view, using the test to act as a view
checking if the HTTP_REQUEST was correct for that view
"""


class TestIndexPage(TestCase, views.IndexView):

    def test_given_request_when_get_called_check_200(self):
        request = HttpRequest()
        request.method = 'POST'
        response = self.get(request=request)
        self.assertEqual(200, response.status_code)
        self.assertIn("Hello world", response.content.decode('utf-8'))
