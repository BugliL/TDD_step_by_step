import copy


def createStatementData(invoice, plays):
    class PerformanceCalculator(object):
        def __init__(self, aPerformance, aPlay):
            self._performance = aPerformance
            self.play = aPlay

        def __getitem__(self, item):
            return self._performance[item]

    class Performance(object):
        def __init__(self, aPerformance):
            self._performance = copy.deepcopy(aPerformance)
            self.calculator = PerformanceCalculator(self._performance, self.playFor(self._performance))
            self.play = self.playFor(self._performance)
            self.amount = self.amountFor()
            self.credits = self.volumeCreditsFor()

        def playFor(self, aPerformance):
            return plays[aPerformance['playID']]

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

    return StatementData(
        customer=invoice['customer'],
        performances=[Performance(p) for p in invoice['performances']]
    )
