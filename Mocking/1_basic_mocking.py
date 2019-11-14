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
            return
        else:
            raise AssertionError("{} was not raised".format(exception_type))

    def test_basic(self):
        # class unittest.mock.Mock
        mock_object = mock.Mock()
        mock_object.random_attribute = "A mocked attribute"
        self.assertEqual(mock_object.random_attribute, "A mocked attribute")

    def test_called(self):
        # assert_called is used to check if Mock is used as call
        mock_object = mock.Mock()

        # at this point "method" is not called so it raises an error
        self.assertRaises(AssertionError, mock_object.method.assert_called)

        # now is called
        mock_object.method()

        # and do not raise an exception anymore
        # these lines are equivalent
        mock_object.method.assert_called()
        self.assertNotRaises(AssertionError, mock_object.method.assert_called)
