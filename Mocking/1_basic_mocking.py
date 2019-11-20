import unittest

# From official documentation of standard library
# Mock and MagicMock objects create all attributes and methods as you access them
# and store details of how they have been used.

# The Mock Class
from unittest import mock


# Mock is a flexible mock object intended to replace the use of stubs and test
# doubles throughout your code.


class BasicTesting(unittest.TestCase):

    def test_basic(self):
        # class unittest.mock.Mock
        mock_object = mock.Mock()
        mock_object.random_attribute = "A mocked attribute"
        self.assertEqual(mock_object.random_attribute, "A mocked attribute")

    def test_attributes(self):
        # The main characteristic of a Mock object is that it will return another Mock instance when:
        #   - accessing one of its attributes
        #   - calling the object itself
        mock_object = mock.Mock()
        self.assertIsInstance(mock_object.attribute, mock.Mock)
        self.assertIsInstance(mock_object.method(), mock.Mock)
        self.assertIsInstance(mock_object(), mock.Mock)

        # and everytime is a differente object
        self.assertIsNot(mock_object(), mock_object.method())

        # you can assign a value to an attribute in the Mock by:
        #   - direct assign
        #   - configure_mock method (useful if you have a dictionary)
        #   - parameter on creation.
        mock_object = mock.Mock(attribute="hello")
        self.assertEqual("hello", mock_object.attribute)

        mock_object = mock.Mock()
        mock_object.attribute = "hello2"
        self.assertEqual("hello2", mock_object.attribute)

        mock_object = mock.Mock()
        mock_object.configure_mock(attribute="hello3")
        self.assertEqual("hello3", mock_object.attribute)
