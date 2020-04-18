from __future__ import annotations
from decimal import Decimal
from enum import Enum
from uuid import UUID

from domain.classified_ad_id import ClassifiedAdId
from domain.classified_ad_text import ClassifiedAdText
from domain.classified_ad_title import ClassifiedAdTitle
from domain.price import Price
from domain.user_id import UserId


class ClassifiedAdStatus(Enum):
    Inactive = 'INACTIVE'
    PendingReview = 'PENDINGREVIEW'
    Active = 'ACTIVE'
    MarkedAsSold = 'MARKEDASSOLD'


class ClassifiedAd:
    def __init__(self, id: UUID, owner_id: UUID):
        self.__id: ClassifiedAdId = ClassifiedAdId(id)
        self.__owner_id: UserId = UserId(owner_id)

        self.__status: ClassifiedAdStatus = ClassifiedAdStatus.Inactive
        self.__title: ClassifiedAdTitle = None
        self.__text: ClassifiedAdText = None
        self.__price: Price = None
        self.__approved_by: UserId = None

        self.__post_init__()

    def set_title(self, title: str):
        self.__title = title
        self.__post_init__()

    def update_text(self, text: str):
        self.__text = text
        self.__post_init__()

    def update_price(self, price: Decimal):
        self.__price = price
        self.__post_init__()

    def request_to_publish(self):
        self.__status = ClassifiedAdStatus.PendingReview
        self.__post_init__()

    def __post_init__(self):
        if (not self.__id) or (not self.__owner_id) or (not self.__status):
            raise ValueError("Invalid state")

        if self.__status == ClassifiedAdStatus.PendingReview:
            if not all([self.__text, self.__title, self.__price]):
                raise ValueError("Invalid state")

        if self.__status == ClassifiedAdStatus.Active:
            if not all([self.__text, self.__title, self.__price, self.__approved_by]):
                raise ValueError("Invalid state")

        if self.__status == ClassifiedAdStatus.Inactive:
            return

    @property
    def id(self) -> ClassifiedAdId:
        return self.__id

    @property
    def status(self) -> ClassifiedAdStatus:
        return self.__status
