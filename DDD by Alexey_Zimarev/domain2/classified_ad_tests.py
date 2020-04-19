import unittest

import uuid

from domain2.classified_ad import ClassifiedAd
from domain2.classified_ad import ClassifiedAdStatus
from domain.classified_ad_text import ClassifiedAdText
from domain.classified_ad_title import ClassifiedAdTitle
from domain.tests.money_tests import FakeCurrencyLookup
from domain.price import Price


# noinspection PyPep8Naming
class ClassifiedAdTest(unittest.TestCase):

    def setUp(self) -> None:
        self.params = {'id': uuid.uuid4(), 'owner_id': uuid.uuid4()}

    def test_given_created_classified_ad_should_no_error_after_creation(self):
        x = ClassifiedAd(**self.params)
        self.assertEqual(ClassifiedAdStatus.Inactive, x.data.status)

    def test_given_classified_ad_with_no_text_should_not_be_published(self):
        x = ClassifiedAd(**self.params)
        x.set_title(ClassifiedAdTitle.create('A title'))
        x.update_price(Price.create(
            amount=10,
            currency='EUR',
            lookup=FakeCurrencyLookup
        ))

        with self.assertRaises(ValueError):
            x.request_to_publish()

    def test_given_classified_ad_with_no_title_should_not_be_published(self):
        x = ClassifiedAd(**self.params)
        x.update_text(ClassifiedAdText.create('A Text'))
        x.update_price(Price.create(
            amount=10,
            currency='EUR',
            lookup=FakeCurrencyLookup
        ))

        with self.assertRaises(ValueError):
            x.request_to_publish()

    def test_given_classified_ad_with_no_price_should_not_be_published(self):
        x = ClassifiedAd(**self.params)
        x.update_text(ClassifiedAdText.create('A Text'))
        x.set_title(ClassifiedAdTitle.create('A title'))

        with self.assertRaises(ValueError):
            x.request_to_publish()
