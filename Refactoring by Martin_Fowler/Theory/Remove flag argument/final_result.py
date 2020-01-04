from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Order:
    delivery_state: str
    placed_on: datetime


@dataclass
class Shipment:
    order: Order
    delivery_date: datetime = datetime.now()


def delivery_date(order: Order, is_rush):
    if is_rush:
        return rush_delivery_date(order)
    else:
        return normal_delivery_date(order)


def normal_delivery_date(order):
    delivery_time = 4
    if order.delivery_state in ['MA', 'CT', 'NY']:
        delivery_time = 2
    elif order.delivery_state in ['ME', 'NH']:
        delivery_time = 3
    return order.placed_on + timedelta(days=delivery_time)


def rush_delivery_date(order):
    delivery_time = 3
    if order.delivery_state in ['MA', 'CT']:
        delivery_time = 1
    elif order.delivery_state in ['NY', 'NH']:
        delivery_time = 2
    return order.placed_on + timedelta(days=delivery_time)


if __name__ == '__main__':
    order = Order(
        delivery_state='MA',
        placed_on=datetime.now()
    )

    shipment = Shipment(order=Order)

    shipment.delivery_date = delivery_date(order, is_rush=True)
    print(shipment.delivery_date)

    shipment.delivery_date = delivery_date(order, is_rush=False)
    print(shipment.delivery_date)
