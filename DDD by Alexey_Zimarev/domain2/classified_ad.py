import uuid
from dataclasses import field, dataclass
from decimal import Decimal
from uuid import UUID

from domain2.entity import EntityEvent, Event
from domain2.events import ClassifiedAdCreated, ClassifiedAdUpdatedText, ClassifiedAdUpdatedTitle, \
    ClassifiedAdRequestedToPublish, ClassifiedAdUpdatedPrice


@dataclass
class ClassifiedAdData:
    id: UUID = field()
    owner_id: UUID = field()
    status: str = field(init=False, default='INACTIVE')
    title: str = field(init=False, default=None)
    text: str = field(init=False, default=None)
    price: Decimal = field(init=False, default=None)


class ClassifiedAd(EntityEvent):
    data: ClassifiedAdData

    def __init__(self, id: UUID, owner_id: UUID):
        super().__init__()

        self.apply(
            ClassifiedAdCreated(
                id=id,
                owner_id=owner_id
            )
        )

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
                id=self.data.id,
                text=text
            )
        )

    def when(self, event: Event):
        def created(cad_event: ClassifiedAdCreated):
            self.data = ClassifiedAdData(cad_event.id, cad_event.owner_id)

        def update_title(cad_event: ClassifiedAdUpdatedTitle):
            self.data.title = cad_event.title

        def update_text(cad_event: ClassifiedAdUpdatedText):
            self.data.text = cad_event.text

        def update_price(cad_event: ClassifiedAdUpdatedPrice):
            self.data.price = Decimal(cad_event.price)

        def requested_to_publish(cad_event: ClassifiedAdRequestedToPublish):
            self.data.status = "PENDING"

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
