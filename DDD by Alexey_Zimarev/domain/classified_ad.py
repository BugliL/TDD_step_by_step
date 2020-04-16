from decimal import Decimal
from uuid import UUID


class ClassifiedAd:

    def __init__(self, id: UUID):
        self.__id: UUID = id

        self.__ownerId: UUID = None
        self.__title: str = None
        self.__text: str = None
        self.__price: Decimal = None

    # Added behavior to update attributes
    def set_title(self, title: str):
        self.__title = title

    def update_text(self, text: str):
        self.__text = text

    def update_price(self, price: Decimal):
        self.__price = price

    @property
    def id(self) -> UUID:
        return self.__id


if __name__ == '__main__':
    import uuid

    x = ClassifiedAd(id=uuid.uuid4())
    print(x.id)
