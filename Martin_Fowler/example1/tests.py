import unittest
import json
from .problem import statement


class ProblemTestCase(unittest.TestCase):

    def setUp(self):
        with open("example1/plays.json", 'r') as plays_file:
            self.plays = json.load(plays_file)

        with open("example1/invoices.json", 'r') as invoices_file:
            self.invoices = json.load(invoices_file)

    def test_basic_function(self):
        string = "Statement for BigCo\n" \
                 "    Hamlet: $650.00 (55 seats)\n" \
                 "    As you like it: $580.00 (35 seats)\n" \
                 "    Othello: $500.00 (40 seats)\n" \
                 "Amount owed is ($1,730.00)\n" \
                 "You earned 47 credits\n"

        self.assertEqual(string, statement(self.invoices[0], self.plays))
