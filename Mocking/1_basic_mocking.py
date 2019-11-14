import unittest

# From official documentation of standard library
# Mock and MagicMock objects create all attributes and methods as you access them
# and store details of how they have been used.

# The Mock Class
from unittest import mock


# Mock is a flexible mock object intended to replace the use of stubs and test
# doubles throughout your code.
#
# class unittest.mock.Mock
#   spec=None
#   side_effect=None
#   return_value=DEFAULT
#   wraps=None
#   name=None
#   spec_set=None
#   unsafe=False
#   **kwargs


class BasicTesting(unittest.TestCase):
    def test_basic(self):
        # class unittest.mock.Mock
        mock_object = mock.Mock()
        mock_object.random_attribute = "A mocked attribute"
        self.assertEqual(mock_object.random_attribute, "A mocked attribute")

