from datetime import datetime as dt
from dataclasses import dataclass


@dataclass
class Plan:
    summer_start_date: dt
    summer_end_date: dt

    summer_rate: float
    regular_rate: float


def function_to_refactor(selected_date: dt, plan: Plan, qty):
    def is_summer():
        return plan.summer_start_date < selected_date < plan.summer_end_date

    def summer_charge():
        result = qty * plan.summer_rate
        return result

    def regular_charge():
        result = qty * plan.regular_rate
        return result

    return summer_charge() if is_summer() else regular_charge()


if __name__ == '__main__':
    plan = Plan(
        summer_start_date=dt(2020, 5, 1),
        summer_end_date=dt(2020, 9, 1),
        summer_rate=2.0,
        regular_rate=1.0
    )

    my_date = dt(2020, 6, 4)
    qty = 10

    x = function_to_refactor(
        selected_date=my_date,
        plan=plan, qty=qty
    )

    print(x)
