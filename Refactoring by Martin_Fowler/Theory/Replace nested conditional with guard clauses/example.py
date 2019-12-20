from dataclasses import dataclass


@dataclass
class Employee():
    is_separated: bool
    is_retired: bool


def calculate_amount(employee):
    # Logic to return an amount
    return 42


def pay_amount(employee: Employee):
    if employee.is_separated:
        result = {'amount':0, 'reason_code': "SEP"}
    else:
        if employee.is_retired:
            result = {'amount':0, 'reason_code': "RET"}
        else:
            result = {'amount':calculate_amount(employee), 'reason_code': "A_REASON"}

    return result

