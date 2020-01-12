import json

from Martin_Fowler.example1.model import createStatementData


def usd(amount):
    return '${:,.2f}'.format(amount)


def statement(invoice, plays):
    def renderPlainText(statement_data):
        result = "Statement for {}\n".format(statement_data.customer)
        for perf in statement_data.performances:
            result += "    {}: {} ({} seats)\n".format(
                perf.play['name'], usd(perf.amount / 100), perf['audience']
            )
        result += f"Amount owed is ({usd(statement_data.total_amount / 100)})\n"
        result += f"You earned {statement_data.total_volume_credits} credits\n"
        return result

    return renderPlainText(
        createStatementData(invoice, plays)
    )


# writing this code wasn't easy at the beginning but now
# with logic and presentation separated is much more easier
def html_statement(invoice, plays):
    def renderHtmlText(statement_data):
        result = "<h1>Statement for {}</h1>\n".format(statement_data.customer)
        result += "<table>\n"
        result += "<tr><th>Play</th><th>Seats</th><th>Costs</th></tr>\n"
        for perf in statement_data.performances:
            result += "<tr>"
            result += "<td>{}</td>".format(perf.play['name'])
            result += "<td>{}</td>".format(perf['audience'])
            result += "<td>{}</td>".format(usd(perf.amount / 100))
            result += "</tr>\n"
        result += "</table>\n"
        result += "<p>Amount owed is <em>{}</em></p>\n".format(usd(statement_data.total_amount / 100))
        result += "<p>You earned <em>{}</em> credits</p>\n".format(statement_data.total_volume_credits)
        return result

    return renderHtmlText(
        createStatementData(invoice, plays)
    )


if __name__ == "__main__":
    with open("plays.json", 'r') as plays_file:
        plays = json.load(plays_file)

    with open("invoices.json", 'r') as invoices_file:
        invoices = json.load(invoices_file)

    print(statement(invoices[0], plays))
    print(html_statement(invoices[0], plays))
