from dataclasses import dataclass


@dataclass
class Employee():
    is_separated: bool
    is_retired: bool
    age: int


def calculate_amount(employee):
    # Logic to return an amount
    return 42


def pay_amount(employee: Employee):
    if employee.is_separated:
        result = {'amount': 0, 'reason_code': "SEP"}
    else:
        if employee.is_retired:
            if employee.age < 60:
                result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}
            else:
                result = {'amount': 0, 'reason_code': "RET"}
        else:
            result = {'amount': calculate_amount(employee), 'reason_code': "A_REASON"}

    return result


if __name__ == '__main__':
    employee = Employee(
        is_separated=False,
        is_retired=True,
        age=67
    )

    print(pay_amount(employee))
