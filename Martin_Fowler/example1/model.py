import copy


def createStatementData(invoice, plays):
    class PerformanceCalculator(object):
        def __init__(self, aPerformance):
            self._performance = copy.deepcopy(aPerformance)
            self.play = self.playFor(self._performance)

        def playFor(self, aPerformance):
            return plays[aPerformance['playID']]

        @property
        def amount(self):
            if self.play['type'] == "tragedy":
                result = self._tragedyAmount()
            elif self.play['type'] == "comedy":
                result = self._comedyAmount()
            else:
                raise Exception(f"uknown type: {self.play['type']}")
            return result

        def _tragedyAmount(self):
            raise NotImplementedError()
            # result = 40000
            # if self['audience'] > 30:
            #     result += 1000 * (self['audience'] - 30)
            # return result

        def _comedyAmount(self):
            result = 30000
            if self['audience'] > 20:
                result += 10000 + 500 * (self['audience'] - 20)
            result += 300 * self['audience']
            return result

        @property
        def volumeCredits(self):
            result = max(self['audience'] - 30, 0)
            if "comedy" == self.play['type']: result += round(self['audience'] / 5)
            return result

        def __getitem__(self, item):
            return self._performance[item]

    class TragedyPerformanceCalculator(PerformanceCalculator):
        @property
        def amount(self):
            result = 40000
            if self['audience'] > 30:
                result += 1000 * (self['audience'] - 30)
            return result

    class ComedyPerformanceCalculator(PerformanceCalculator):
        @property
        def amount(self):
            result = 30000
            if self['audience'] > 20:
                result += 10000 + 500 * (self['audience'] - 20)
            result += 300 * self['audience']
            return result

    def createPerformanceCalculator(aPerformance):
        def playFor(aPerformance):
            return plays[aPerformance['playID']]

        calculators = {
            "tragedy": TragedyPerformanceCalculator,
            "comedy": ComedyPerformanceCalculator,
        }
        calc = calculators.get(playFor(aPerformance)["type"], None)
        if calc is None:
            raise Exception("uknown type: {}".format(playFor(aPerformance)["type"]))

        return calc(aPerformance)

    class Performance(object):
        def __init__(self, aPerformance):
            self._performance = copy.deepcopy(aPerformance)
            self.calculator = createPerformanceCalculator(self._performance)
            self.play = self.calculator.play
            self.amount = self.calculator.amount
            self.credits = self.calculator.volumeCredits

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
