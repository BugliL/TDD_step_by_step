"""
.TODO LIST
    - Add amount of different values
    - Money rounding

    - equals
        - Equal null
        - Equal object
    - hashCode
    - $5 + 10CHF = $10 if rate is 2:test1
    - $5 + $5 = $10

    * Multiply amounts Dollars
    * Multiply amounts Franc
    * Amount private
    * Check side effects
    * equals
        * common equal
    * compare dollars and francs
    * $5 * 2 = $10
    * Dollar / Franc duplication


"""

import unittest

from test1.problem import MoneyFactory, Bank


class TestFrancDollarTogether(unittest.TestCase):
    def test_given_dollars_and_francs_when_compared_result_different(self):
        self.assertNotEqual(MoneyFactory.dollar(5), MoneyFactory.franc(5))


class TestFranc(unittest.TestCase):
    def test_given_5franc_when_called_times2_than_eq_10franc(self):
        x = MoneyFactory.franc(5)
        self.assertEqual(x.times(2), MoneyFactory.franc(10))

    def test_given_5CHD_and_5CHD_when_reduced_by_bank_than_return_10CHD(self):
        f1 = MoneyFactory.franc(5)
        expression = f1 + f1
        reduced_expression = expression.convert('CHD')
        self.assertEqual(reduced_expression, MoneyFactory.franc(10))

    def test_given_10CHD_when_converted_to_USD_than_result_5USD(self):
        f1 = MoneyFactory.franc(10)
        self.assertEqual(f1.convert('USD'), MoneyFactory.dollar(5))

    def test_given_5CHD_and_5CHD_when_sum_than_return_10CHD(self):
        f1 = MoneyFactory.franc(5)
        f2 = MoneyFactory.franc(5)
        self.assertEqual(f1 + f2, MoneyFactory.franc(10))

    def test_given_5franc_when_created_than_eq_5franc_and_neq_6franc(self):
        self.assertEqual(MoneyFactory.franc(5), MoneyFactory.franc(5))
        self.assertNotEqual(MoneyFactory.franc(6), MoneyFactory.franc(5))

    def test_given_aFranc_when_created_than_amount_accessible_readonly(self):
        x = MoneyFactory.franc(1)
        self.assertEqual(1, x.amount)

        x.amount = 5
        self.assertNotEqual(5, x.amount)
        self.assertEqual(1, x.amount)

    def test_given_aFranc_when_created_than_currency_accessible_readonly(self):
        x = MoneyFactory.franc(1)
        self.assertEqual('CHD', x.currency)

        x.currency = 'USD'
        self.assertNotEqual('USD', x.currency)
        self.assertEqual('CHD', x.currency)


class TestDollar(unittest.TestCase):
    def test_given_5USD_and_5USD_when_sum_than_return_10USD(self):
        d1 = MoneyFactory.dollar(5)
        d2 = MoneyFactory.dollar(5)
        d3 = MoneyFactory.dollar(5)
        self.assertEqual(d1 + d2 + d3, MoneyFactory.dollar(15))

    def test_given_5USD_when_called_times2_and_times3_than_eq_10USD(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(x.times(3), MoneyFactory.dollar(15))

    def test_given_5USD_when_created_than_eq_5USD_and_neq_6USD(self):
        self.assertEqual(MoneyFactory.dollar(5), MoneyFactory.dollar(5))
        self.assertNotEqual(MoneyFactory.dollar(6), MoneyFactory.dollar(5))


class TestPrint(unittest.TestCase):
    def test_given_aDollar_when_string_converted_than_print_amount_and_USD(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(str(x), "5USD")
