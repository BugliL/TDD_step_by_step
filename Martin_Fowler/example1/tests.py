import unittest
import json
from .problem import statement, html_statement


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

    def test_html_function(self):
        string = "<h1>Statement for BigCo</h1>\n" \
                 "<table>\n" \
                 "<tr><th>Play</th><th>Seats</th><th>Costs</th></tr>\n" \
                 "<tr><td>Hamlet</td><td>55</td><td>$650.00</td></tr>\n" \
                 "<tr><td>As you like it</td><td>35</td><td>$580.00</td></tr>\n" \
                 "<tr><td>Othello</td><td>40</td><td>$500.00</td></tr>\n" \
                 "</table>\n" \
                 "<p>Amount owed is <em>$1,730.00</em></p>\n" \
                 "<p>You earned <em>47</em> credits</p>\n"

        self.assertEqual(string, html_statement(self.invoices[0], self.plays))