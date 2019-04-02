import json

from .model import createStatementData


def usd(amount):
    return '${:,.2f}'.format(amount)


def statement(invoice, plays):
    def renderPlainText(statement_data):
        result = "Statement for {}\n".format(statement_data.customer)
        for perf in statement_data.performances:
            result += f"    {perf.play['name']}: {usd(perf.amount/100)} ({perf['audience']} seats)\n"
        result += f"Amount owed is ({usd(statement_data.total_amount/100)})\n"
        result += f"You earned {statement_data.total_volume_credits} credits\n"
        return result

    return renderPlainText(
        createStatementData(invoice, plays)
    )


if __name__ == "__main__":
    with open("plays.json", 'r') as plays_file:
        plays = json.load(plays_file)

    with open("invoices.json", 'r') as invoices_file:
        invoices = json.load(invoices_file)

    print(statement(invoices[0], plays))
