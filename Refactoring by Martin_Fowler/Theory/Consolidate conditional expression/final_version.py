class Employee:
    seniority: int = 1
    months_unavailable: int = 24
    is_part_time: True
    work_hours: int = 9


def calculate_amount(employee: Employee):
    if employee.seniority < 2 \
            or employee.months_unavailable > 12: return 0

    if employee.is_part_time \
            and employee.work_hours > 8: return 0

    return 10


if __name__ == '__main__':
    employee = Employee()
    amount = calculate_amount(employee)
    print(amount)
