import decimal
import uuid


class ClassifiedAd:

    def __init__(self, id: uuid.UUID):
        self.id: uuid.UUID = id

        self.ownerId: uuid.UUID = None
        self.title: str = None
        self.text: str = None
        self.price: decimal.Decimal = None


if __name__ == '__main__':
    x = ClassifiedAd(id=uuid.uuid4())
