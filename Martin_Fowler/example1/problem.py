import json


def statement(invoice, plays):
    def playFor(aPerformance):
        return plays[aPerformance['playID']]

    def amountFor(aPerformance):
        result = 0
        if playFor(aPerformance)['type'] == "tragedy":
            result = 40000
            if aPerformance['audience'] > 30:
                result += 1000 * (aPerformance['audience'] - 30)
        elif playFor(aPerformance)['type'] == "comedy":
            result = 30000
            if aPerformance['audience'] > 20:
                result += 10000 + 500 * (aPerformance['audience'] - 20)
            result += 300 * aPerformance['audience']
        else:
            raise Exception(f"uknown type: {playFor(aPerformance)['type']}")
        return result

    def volumeCreditsFor(aPerformance):
        result = max(aPerformance['audience'] - 30, 0)
        if "comedy" == playFor(aPerformance)['type']: result += round(aPerformance['audience'] / 5)
        return result

    def usd(amount):
        return '${:,.2f}'.format(amount)

    def totalVolumeCredits():
        result = 0
        for perf in invoice['performances']:
            result += volumeCreditsFor(perf)
        return result

    def totalAmount():
        result = 0
        for perf in invoice['performances']:
            result += amountFor(perf)
        return result

    result = f"Statement for {invoice['customer']}\n"
    total_amount = totalAmount()

    for perf in invoice['performances']:
        result += f"    {playFor(perf)['name']}: {usd(amountFor(perf)/100)} ({perf['audience']} seats)\n"

    result += f"Amount owed is ({usd(total_amount/100)})\n"
    result += f"You earned {totalVolumeCredits()} credits\n"
    return result


if __name__ == "__main__":
    with open("plays.json", 'r') as plays_file:
        plays = json.load(plays_file)

    with open("invoices.json", 'r') as invoices_file:
        invoices = json.load(invoices_file)

    print(statement(invoices[0], plays))