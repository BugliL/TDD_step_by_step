import unittest

from dj.drf_error_handling.models import FieldJsonError, FieldJsonErrorList


class ErrorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.error_class = 'aClass'
        self.error_code = 'ValueError'
        self.error_message = 'Il codice non e\' valido'
        self.error_name = 'name'
        self.maxDiff = None

        self.error = FieldJsonError(
            classe=self.error_class,
            name=self.error_name,
            code=self.error_code,
            error=self.error_message
        )

    def tearDown(self) -> None:
        FieldJsonErrorList.reset()

    def test_creation(self):
        self.assertEqual(self.error_name, self.error.name)
        self.assertEqual(self.error_code, self.error.code)
        self.assertEqual(self.error_message, self.error.error)
        self.assertEqual(self.error_class, self.error.classe)

    def test_representation(self):
        import json

        result_dict = {
            self.error_class: {
                self.error_name: {
                    'code': self.error_code,
                    'error': self.error_message
                }
            }
        }

        self.assertDictEqual(result_dict, json.loads(str(self.error)))

    def test_error_group(self):
        a1 = {'classe': 'class_a', 'name': 'name_a', 'code': self.error_code, 'error': self.error_message}
        a2 = {'classe': 'class_a', 'name': 'name_b', 'code': self.error_code, 'error': self.error_message}
        b = {'classe': 'class_b', 'name': 'name_b', 'code': self.error_code, 'error': self.error_message}
        c = {'classe': 'class_c', 'name': 'name_c', 'code': self.error_code, 'error': self.error_message}

        FieldJsonErrorList.add(**a1)
        FieldJsonErrorList.add(**a2)
        FieldJsonErrorList.add(**b)
        FieldJsonErrorList.add(**c)

        results = {
            'class_a': {
                'name_a': {'code': self.error_code, 'error': self.error_message},
                'name_b': {'code': self.error_code, 'error': self.error_message},
            },
            'class_b': {
                'name_b': {'code': self.error_code, 'error': self.error_message},
            },
            'class_c': {
                'name_c': {'code': self.error_code, 'error': self.error_message},
            },
            'global': {'code': '', 'error': ''}
        }

        self.assertDictEqual(results, FieldJsonErrorList.asdict())

    def test_raise(self):
        try:
            # FieldJsonErrorList.raise_error()
            pass
        except:
            self.fail('Exception raised, test failed')

        FieldJsonErrorList.add(classe='base', name='field1', code=self.error_code, error=self.error_message)
        self.assertRaises(Exception, FieldJsonErrorList.raise_error)


if __name__ == '__main__':
    ErrorTestCase()
