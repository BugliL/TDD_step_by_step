import unittest

from domain.classified_ad_title import ClassifiedAdTitle


class ClassifiedAdTitleTest(unittest.TestCase):

    def test_given_more_than_100_char_title_should_raise_excption(self):
        ClassifiedAdTitle("5" * 99)
        with self.assertRaises(ValueError):
            ClassifiedAdTitle("5" * 120)

    def test_factory_method(self):
        string_title = 'Zanna bianca'
        x = ClassifiedAdTitle(string_title)
        self.assertEqual(string_title, str(x))


if __name__ == '__main__':
    pass
