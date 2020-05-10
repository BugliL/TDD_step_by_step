import unittest

from dj.drf_error_handling.models import FieldJsonError, FieldJsonErrorList


class ErrorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.error_code = 'ValueError'
        self.error_message = 'Il codice non e\' valido'
        self.error_name = 'name'

        self.error = FieldJsonError(
            name=self.error_name,
            code=self.error_code,
            message=self.error_message
        )

    def tearDown(self) -> None:
        FieldJsonErrorList.reset()

    def test_creation(self):
        self.assertEqual(self.error_name, self.error.name)
        self.assertEqual(self.error_code, self.error.code)
        self.assertEqual(self.error_message, self.error.message)

    def test_representation(self):
        import json

        result_dict = {
            self.error_name: {
                'code': self.error_code,
                'message': self.error_message
            }
        }

        self.assertDictEqual(result_dict, json.loads(str(self.error)))

    def test_error_group(self):
        a = {'name': 'name_a', 'code': self.error_code, 'message': self.error_message}
        b = {'name': 'name_b', 'code': self.error_code, 'message': self.error_message}
        c = {'name': 'name_c', 'code': self.error_code, 'message': self.error_message}

        FieldJsonErrorList.add(**a)
        FieldJsonErrorList.add(**b)
        FieldJsonErrorList.add(**c)

        results = {
            'name_a': {'code': self.error_code, 'message': self.error_message},
            'name_b': {'code': self.error_code, 'message': self.error_message},
            'name_c': {'code': self.error_code, 'message': self.error_message},
            'global': {'code': '', 'message': ''}
        }

        self.assertDictEqual(results, FieldJsonErrorList.asdict())

    def test_raise(self):
        try:
            FieldJsonErrorList.raise_error()
        except:
            self.fail('Exception raised, test failed')

        FieldJsonErrorList.add(name='field1', code=self.error_code, message=self.error_message)
        self.assertRaises(Exception, FieldJsonErrorList.raise_error)


if __name__ == '__main__':
    ErrorTestCase()
