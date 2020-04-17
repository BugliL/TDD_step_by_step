from decimal import Decimal
from uuid import UUID

from domain.classified_ad_id import ClassifiedAdId
from domain.user_id import UserId


class ClassifiedAd:

    def __init__(self, id: UUID, ownerId: UUID):
        self.__id: ClassifiedAdId = ClassifiedAdId(id)
        self.__ownerId: UserId = UserId(ownerId)

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
