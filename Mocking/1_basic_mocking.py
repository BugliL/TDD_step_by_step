import unittest

# From official documentation of standard library
# Mock and MagicMock objects create all attributes and methods as you access them
# and store details of how they have been used.

# The Mock Class
from unittest import mock


# Mock is a flexible mock object intended to replace the use of stubs and test
# doubles throughout your code.


class BasicTesting(unittest.TestCase):

    def assertNotRaises(self, exception_type, *args, **kwargs):
        try:
            # this code raise AssertionError if *args, **kwargs
            # is not raising an exception
            self.assertRaises(exception_type, *args, **kwargs)
        except exception_type:
            self.assertTrue(True)
        else:
            self.fail("{} was not raised".format(exception_type))

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

    def test_called(self):
        # assert_called is used to check if Mock is used as call
        mock_object = mock.Mock()

        # at this point "method" is not called so it raises an error
        # (method is not defined but it don't raise an error)
        self.assertRaises(AssertionError, mock_object.method.assert_called)

        # now is called
        mock_object.method()

        # and do not raise an exception anymore
        # these lines are equivalent
        mock_object.method.assert_called()
        self.assertNotRaises(AssertionError, mock_object.method.assert_called)
