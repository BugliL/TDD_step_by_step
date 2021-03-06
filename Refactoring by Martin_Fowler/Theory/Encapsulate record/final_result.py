import copy

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


class RecordData():
    def __init__(self, records):
        self._records = records

    def get_records(self):
        return copy.deepcopy(self._records)

    def set_usage_value(self, customer_id, year, month, value):
        self._records[customer_id]['usages'][year][month] = value

    def get_usage_value(self, customer_id, year, month):
        return self._records[customer_id]['usages'][year][month]


record_data_object = RecordData(records=raw_records)


def get_raw_records():
    return record_data_object.get_records()


def get_records_object():
    return record_data_object


# Update example
get_records_object().set_usage_value(customer_id='9201', year=2016, month=2, value=42)


# Reading example
def compare_usage(customer_id, year, month):
    year_value = get_records_object().get_usage_value(customer_id, year, month)
    last_year_value = get_records_object().get_usage_value(customer_id, year - 1, month)
    return {'amount': year_value, 'difference': year_value - last_year_value}


if __name__ == '__main__':
    d = compare_usage(
        customer_id='9202',
        year=2016,
        month=2
    )
    print(d)
