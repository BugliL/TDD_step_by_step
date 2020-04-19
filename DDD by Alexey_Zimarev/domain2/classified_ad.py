from __future__ import annotations
import uuid
from dataclasses import field, dataclass
from decimal import Decimal
from enum import Enum
from uuid import UUID

from domain2.entity import EntityEvent
from domain2.events import ClassifiedAdCreated, ClassifiedAdUpdatedText, ClassifiedAdUpdatedTitle, \
    ClassifiedAdRequestedToPublish, ClassifiedAdUpdatedPrice


class ClassifiedAdStatus(Enum):
    Inactive = 'INACTIVE'
    PendingReview = 'PENDINGREVIEW'
    Active = 'ACTIVE'
    MarkedAsSold = 'MARKEDASSOLD'


@dataclass
class ClassifiedAdData:
    id: UUID = field()
    owner_id: UUID = field()
    status: str = field(init=False, default=ClassifiedAdStatus.Inactive)
    title: str = field(init=False, default=None)
    text: str = field(init=False, default=None)
    price: Decimal = field(init=False, default=None)
    approved_by: UUID = field(init=False, default=None)


class ClassifiedAdEventManager:

    @classmethod
    def callbacks(cls):
        return {
            ClassifiedAdCreated: cls.created,
            ClassifiedAdUpdatedTitle: cls.update_title,
            ClassifiedAdUpdatedText: cls.update_text,
            ClassifiedAdUpdatedPrice: cls.update_price,
            ClassifiedAdRequestedToPublish: cls.requested_to_publish
        }

    @staticmethod
    def created(classified_ad, cad_event: ClassifiedAdCreated):
        classified_ad.data = ClassifiedAdData(cad_event.id, cad_event.owner_id)
        classified_ad.data.status = ClassifiedAdStatus.Inactive

    @staticmethod
    def update_title(classified_ad, cad_event: ClassifiedAdUpdatedTitle):
        classified_ad.data.title = cad_event.title

    @staticmethod
    def update_text(classified_ad, cad_event: ClassifiedAdUpdatedText):
        classified_ad.data.text = cad_event.text

    @staticmethod
    def update_price(classified_ad, cad_event: ClassifiedAdUpdatedPrice):
        classified_ad.data.price = Decimal(cad_event.price)

    @staticmethod
    def requested_to_publish(classified_ad, cad_event: ClassifiedAdRequestedToPublish):
        classified_ad.data.status = ClassifiedAdStatus.PendingReview


def ensure_valid_state(self: ClassifiedAd):
    if (not self.data.id) or (not self.data.owner_id) or (not self.data.status):
        raise ValueError("Invalid state")

    if self.data.status == ClassifiedAdStatus.PendingReview:
        if not all([self.data.text, self.data.title, self.data.price]):
            raise ValueError("Invalid state")

    if self.data.status == ClassifiedAdStatus.Active:
        if not all([
            self.data.text,
            self.data.title,
            self.data.price,
            self.data.approved_by]
        ):
            raise ValueError("Invalid state")

    if self.data.status == ClassifiedAdStatus.Inactive:
        return


class ClassifiedAd(EntityEvent):
    def __init__(self, id: UUID, owner_id: UUID):
        super().__init__()
        self.data: ClassifiedAdData = None
        self.callbacks = ClassifiedAdEventManager.callbacks()
        self.__class__.ensure_valid_state = ensure_valid_state
        self.apply(ClassifiedAdCreated(id=id, owner_id=owner_id))

    def set_title(self, title: str):
        self.apply(
            ClassifiedAdUpdatedTitle(
                id=self.data.id,
                title=title
            )
        )

    def update_text(self, text: str):
        self.apply(
            ClassifiedAdUpdatedText(
                id=self.data.id, text=text
            )
        )

    def update_price(self, text: str):
        self.apply(
            ClassifiedAdUpdatedText(
                id=self.data.id, text=text
            )
        )

    def request_to_publish(self):
        self.apply(
            ClassifiedAdRequestedToPublish(
                id=self.data.id,
            )
        )


if __name__ == '__main__':
    from pprint import pprint

    x = ClassifiedAd(id=uuid.uuid4(), owner_id=uuid.uuid4())
    pprint(x.events)
    x.update_text('Ciao')
    pprint(x.events)
    pprint(x.data)
