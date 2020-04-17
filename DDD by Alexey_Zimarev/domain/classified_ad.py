from decimal import Decimal
from uuid import UUID


class ClassifiedAd:

    def __init__(self, id: UUID, ownerId: UUID):

        if not id:
            raise ValueError("id must be set correctly")

        if not ownerId:
            raise ValueError("ownerId must be set correctly")

        self.__id: UUID = id
        self.__ownerId: UUID = ownerId

        self.__title: str = None
        self.__text: str = None
        self.__price: Decimal = None

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

    x = ClassifiedAd(id=uuid.uuid4(), ownerId=uuid.uuid4())
    print(x.id)
