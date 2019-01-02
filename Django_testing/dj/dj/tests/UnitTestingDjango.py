from django.test import TestCase
from django.urls import resolve

from .. import views


class UrlsTestCases(TestCase):
    """
        - Accept HTTP requests at certain urls
        - Route those to the appropiate functions
        - Access system resources as necessary to fulfill the logic in those functions
        - Return valid HTTP response
    """

    def test_given_root_url_when_called_index_view_rendered(self):
        root = resolve('dj:index')
        self.assertEqual(root.func, views.function_index)
