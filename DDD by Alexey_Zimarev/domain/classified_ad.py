from decimal import Decimal
from uuid import UUID

from domain.classified_ad_id import ClassifiedAdId
from domain.user_id import UserId


class ClassifiedAd:

    def __init__(self, id: UUID, owner_id: UUID):
        self.__id: ClassifiedAdId = ClassifiedAdId(id)
        self.__owner_id: UserId = UserId(owner_id)

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
    def id(self) -> ClassifiedAdId:
        return self.__id
