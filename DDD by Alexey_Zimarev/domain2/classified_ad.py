import uuid
from dataclasses import field, dataclass
from decimal import Decimal
from enum import Enum
from uuid import UUID

from domain2.entity import EntityEvent, Event
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


class ClassifiedAd(EntityEvent):
    def __init__(self, id: UUID, owner_id: UUID):
        super().__init__()
        self.data: ClassifiedAdData = None
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

    def ensure_valid_state(self):
        if (not self.data.id) or (not self.data.owner_id) or (not self.data.status):
            raise ValueError("Invalid state")

        if self.data.status == ClassifiedAdStatus.PendingReview:
            if not all([self.data.text, self.data.title, self.data.price]):
                raise ValueError("Invalid state")

        if self.data.status == ClassifiedAdStatus.Active:
            if not all([self.data.text, self.data.title, self.data.price, self.data.approved_by]):
                raise ValueError("Invalid state")

        if self.data.status == ClassifiedAdStatus.Inactive:
            return

    def when(self, event: Event):
        def created(cad_event: ClassifiedAdCreated):
            self.data = ClassifiedAdData(cad_event.id, cad_event.owner_id)
            self.data.status = ClassifiedAdStatus.Inactive

        def update_title(cad_event: ClassifiedAdUpdatedTitle):
            self.data.title = cad_event.title

        def update_text(cad_event: ClassifiedAdUpdatedText):
            self.data.text = cad_event.text

        def update_price(cad_event: ClassifiedAdUpdatedPrice):
            self.data.price = Decimal(cad_event.price)

        def requested_to_publish(cad_event: ClassifiedAdRequestedToPublish):
            self.data.status = ClassifiedAdStatus.PendingReview

        {
            ClassifiedAdCreated: created,
            ClassifiedAdUpdatedTitle: update_title,
            ClassifiedAdUpdatedText: update_text,
            ClassifiedAdUpdatedPrice: update_price,
            ClassifiedAdRequestedToPublish: requested_to_publish
        }.get(event.__class__)(event)


if __name__ == '__main__':
    from pprint import pprint

    x = ClassifiedAd(id=uuid.uuid4(), owner_id=uuid.uuid4())
    pprint(x.events)
    x.update_text('Ciao')
    pprint(x.events)
    pprint(x.data)
    x.request_to_publish()
