import copy
import json


def statement(invoice, plays):


    def volumeCreditsFor(aPerformance):
        result = max(aPerformance['audience'] - 30, 0)
        if "comedy" == aPerformance.play['type']: result += round(aPerformance['audience'] / 5)
        return result

    def usd(amount):
        return '${:,.2f}'.format(amount)

    def totalVolumeCredits(performances):
        result = 0
        for perf in performances:
            result += volumeCreditsFor(perf)
        return result

    def totalAmount(performances):
        result = 0
        for perf in performances:
            result += perf.amount
        return result

    def renderPlainText(statement_data):
        result = "Statement for {}\n".format(statement_data.customer)
        for perf in statement_data.performances:
            result += f"    {perf.play['name']}: {usd(perf.amount/100)} ({perf['audience']} seats)\n"
        result += f"Amount owed is ({usd(totalAmount(statement_data.performances)/100)})\n"
        result += f"You earned {totalVolumeCredits(statement_data.performances)} credits\n"
        return result

    class Performance(object):
        def __init__(self, aPerformance):
            self._performance = copy.deepcopy(aPerformance)
            self.play = self.playFor(self)
            self.amount = self.amountFor(self)

        def playFor(self, aPerformance):
            return plays[aPerformance['playID']]

        def amountFor(self, aPerformance):
            if aPerformance.play['type'] == "tragedy":
                result = 40000
                if aPerformance['audience'] > 30:
                    result += 1000 * (aPerformance['audience'] - 30)
            elif aPerformance.play['type'] == "comedy":
                result = 30000
                if aPerformance['audience'] > 20:
                    result += 10000 + 500 * (aPerformance['audience'] - 20)
                result += 300 * aPerformance['audience']
            else:
                raise Exception(f"uknown type: {aPerformance.play['type']}")
            return result

        def __getitem__(self, item):
            return self._performance[item]

    class StatementData(object):
        def __init__(self, customer, performances):
            self.customer = customer
            self.performances = performances

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
