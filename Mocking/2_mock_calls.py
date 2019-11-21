import unittest
from unittest import mock


# To override calls to the mock you’ll need to configure its return_value
# by the init method or setting the attribute

class MockCallsTesting(unittest.TestCase):
    def assertNotRaises(self, exception_type, *args, **kwargs):
        try:
            # this code raise AssertionError if *args, **kwargs
            # is not raising an exception
            self.assertRaises(exception_type, *args, **kwargs)
        except exception_type:
            self.assertTrue(True)
        else:
            self.fail("{} was not raised".format(exception_type))

    def test_set_side_effects_as_value(self):
        # is possible to set an iterable so that each call correspond to a fixed value.
        # when all values are called, it raises a StopIteration exception
        mock_object = mock.Mock(side_effect=[42, 44, 46, ])

        # these are calls results
        self.assertEqual(42, mock_object())
        self.assertEqual(44, mock_object())
        self.assertEqual(46, mock_object())
        self.assertRaises(StopIteration, mock_object)

        # to return a fixed value when called, set the attribute "return_value"
        mock_object = mock.Mock(return_value=42)
        self.assertEqual(42, mock_object())
        self.assertEqual(42, mock_object())
        self.assertNotEqual(43, mock_object())

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
        mock_object.method.assert_called_once()
        self.assertNotRaises(AssertionError, mock_object.method.assert_called)

