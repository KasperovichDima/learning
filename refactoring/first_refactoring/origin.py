from statement_data import create_satement_data


plays_json = dict(
    hamlet=dict(name='Hamlet', type='tragedy'),
    as_like=dict(name='As You Like It', type='comedy'),
    othello=dict(name='Othello', type='tragedy'),
)

invoices_json = dict(
    customer="BigCo",
    performances=[
        dict(
            play_id='hamlet',
            audience=55
        ),
        dict(
            play_id='as_like',
            audience=35
        ),
        dict(
            play_id='othello',
            audience=40
        ),
    ]
)


def html_statement(invoice, plays):
    return render_html(create_satement_data(invoice, plays))


def render_html(st_data):
    result = f'<hl>Statement for {st_data["customer"]}</hl>\n'
    result += '<table>\n'
    result += '<tr><th>play</th><th>seats</th><th>cost</th></tr>'
    for perf in st_data['performances']:
        result += f"<tr><td>{perf['play']['name']}</td>"
        result += f"<td>{perf['audience']}</td>"
        result += f"<td>{perf['amount']}</td></tr>\n"
    result += '</table>\n'
    result += '<p>Amount owed is  '
    result += f"<em>${st_data['total_amount']}</em></p>\n"
    result += f"<p>You earned <em>${st_data['total_volume_credits']}"
    result += '</em> credits</p>\n'
    return result


def statement(invoice: dict[str, str | int], plays) -> str:

    return render_text(create_satement_data(invoice, plays))


def render_text(st_data: dict) -> str:
    result = f'Statement for {st_data["customer"]}\n'

    for performance in st_data['performances']:
        result += f'  {performance["play"]["name"]}'\
                  f': ${performance["amount"] / 100} '
        result += f'({performance["audience"]} seats)\n'

    result += f'Amount owed is ${st_data["total_amount"] / 100}\n'
    result += f'You earned {st_data["total_volume_credits"]} credits\n'
    return result


reference = ('Statement for BigCo\n'
             '  Hamlet: $650.0 (55 seats)\n'
             '  As You Like It: $580.0 (35 seats)\n'
             '  Othello: $500.0 (40 seats)\n'
             'Amount owed is $1730.0\n'
             'You earned 47 credits\n')


def test_siple():
    print(statement(invoices_json, plays_json))
    assert statement(invoices_json, plays_json) == reference
    print('passed!')

    print(html_statement(invoices_json, plays_json))


def main():
    test_siple()


if __name__ == '__main__':
    main()
