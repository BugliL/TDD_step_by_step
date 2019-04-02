import copy
import json


def statement(invoice, plays):
    def usd(amount):
        return '${:,.2f}'.format(amount)

    def renderPlainText(statement_data):
        result = "Statement for {}\n".format(statement_data.customer)
        for perf in statement_data.performances:
            result += f"    {perf.play['name']}: {usd(perf.amount/100)} ({perf['audience']} seats)\n"
        result += f"Amount owed is ({usd(statement_data.total_amount/100)})\n"
        result += f"You earned {statement_data.total_volume_credits} credits\n"
        return result

    class Performance(object):
        def __init__(self, aPerformance):
            self._performance = copy.deepcopy(aPerformance)
            self.play = self.playFor()
            self.amount = self.amountFor()
            self.credits = self.volumeCreditsFor()

        def playFor(self):
            return plays[self['playID']]

        def amountFor(self):
            if self.play['type'] == "tragedy":
                result = 40000
                if self['audience'] > 30:
                    result += 1000 * (self['audience'] - 30)
            elif self.play['type'] == "comedy":
                result = 30000
                if self['audience'] > 20:
                    result += 10000 + 500 * (self['audience'] - 20)
                result += 300 * self['audience']
            else:
                raise Exception(f"uknown type: {self.play['type']}")
            return result

        def volumeCreditsFor(self):
            result = max(self['audience'] - 30, 0)
            if "comedy" == self.play['type']: result += round(self['audience'] / 5)
            return result

        def __getitem__(self, item):
            return self._performance[item]

    class StatementData(object):
        def __init__(self, customer, performances):
            self.customer = customer
            self.performances = performances
            self.total_amount = self.totalAmount(performances)
            self.total_volume_credits = self.totalVolumeCredits(performances)

        def totalAmount(self, performances):
            return sum([p.amount for p in performances])

        def totalVolumeCredits(self, performances):
            return sum([p.credits for p in performances])

    statement_data = StatementData(
        customer=invoice['customer'],
        performances=[Performance(p) for p in invoice['performances']]
    )

    return renderPlainText(statement_data)


if __name__ == "__main__":
    with open("plays.json", 'r') as plays_file:
        plays = json.load(plays_file)

    with open("invoices.json", 'r') as invoices_file:
        invoices = json.load(invoices_file)

    print(statement(invoices[0], plays))
