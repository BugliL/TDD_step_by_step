import json

with open("example1/plays.json", 'r') as plays_file:
    plays = json.load(plays_file)


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice['customer']}\n"
    format = '${:,.2f}'

    for perf in invoice['performances']:
        this_amount = amountFor(perf)

        volume_credits += max(perf['audience'] - 30, 0)
        if "comedy" == playFor(perf)['type']: volume_credits += round(perf['audience'] / 5)

        result += f"    {playFor(perf)['name']}: {format.format(this_amount/100)} ({perf['audience']} seats)\n"
        total_amount += this_amount

    result += f"Amount owed is ({format.format(total_amount/100)})\n"
    result += f"You earned {volume_credits} credits\n"
    return result


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


if __name__ == "__main__":
    with open("plays.json", 'r') as plays_file:
        plays = json.load(plays_file)

    with open("invoices.json", 'r') as invoices_file:
        invoices = json.load(invoices_file)

    print(statement(invoices[0], plays))
