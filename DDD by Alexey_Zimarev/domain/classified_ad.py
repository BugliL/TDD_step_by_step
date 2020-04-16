import decimal
import uuid


class ClassifiedAd:
    id: uuid.UUID
    ownerId: uuid.UUID
    title: str
    text: str
    price: decimal.Decimal


if __name__ == '__main__':
    pass
