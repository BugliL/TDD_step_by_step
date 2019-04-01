import json


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice['customer']}\n"
    format = '${:,.2f}'

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = 0

        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)
            this_amount += 300 * perf['audience']
        else:
            raise Exception(f"uknown type: {play['type']}")

        volume_credits += max(perf['audience'] - 30, 0)
        if "comedy" == play['type']: volume_credits += round(perf['audience'] / 5)

        result += f"    {play['name']}: {format.format(this_amount/100)} ({perf['audience']} seats)\n"
        total_amount += this_amount

    result += f"Amount owed is ({format.format(total_amount/100)})\n"
    result += f"You earned {volume_credits} credits\n"
    return result


if __name__ == "__main__":
    with open("plays.json", 'r') as plays_file:
        plays = json.load(plays_file)

    with open("invoices.json", 'r') as invoices_file:
        invoices = json.load(invoices_file)

    print(statement(invoices[0], plays))
