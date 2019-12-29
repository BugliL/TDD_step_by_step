raw_records = {
    '9201': {
        'name': 'John Smith',
        'id': 9201,
        'usages': {
            2016: {
                1: 42,
                2: 4,
                3: 2,
            },
            2015: {
                1: 2,
                2: 32,
                3: 92,
            }
        }
    },
    '9202': {
        'name': 'Jane Smith',
        'id': 9202,
        'usages': {
            2016: {
                1: 2,
                2: 71,
                3: 19,
            },
            2015: {
                1: 25,
                2: 8,
                3: 5,
            }
        }
    }
}


def get_raw_records():
    return raw_records


# Update example
get_raw_records()['9201']['usages'][2016][2] = 42


# Reading example
def compare_usage(customer_id, year, month):
    year_value = get_raw_records()[customer_id]['usages'][year][month]
    last_year_value = get_raw_records()[customer_id]['usages'][year - 1][month]
    return {'amount': year_value, 'difference': year_value - last_year_value}


if __name__ == '__main__':
    d = compare_usage(
        customer_id='9202',
        year=2016,
        month=2
    )
    print(d)
