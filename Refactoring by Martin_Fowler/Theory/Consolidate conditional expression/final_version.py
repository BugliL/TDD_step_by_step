class Employee:
    seniority: int = 1
    months_unavailable: int = 24
    is_part_time: True
    work_hours: int = 9


def condition(employee):
    return employee.seniority < 2 \
           or employee.months_unavailable > 12 \
           or (employee.is_part_time
               and employee.work_hours > 8)


def calculate_amount(employee: Employee):
    return 0 if condition(employee) else 10


if __name__ == '__main__':
    employee = Employee()
    amount = calculate_amount(employee)
    print(amount)
