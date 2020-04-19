from dataclasses import dataclass
from uuid import UUID

from domain2.entity import Event



@dataclass
class ClassifiedAdCreated(Event):
    id: UUID
    owner_id: UUID


@dataclass
class ClassifiedAdUpdatedText(Event):
    id: UUID
    text: str


@dataclass
class ClassifiedAdUpdatedTitle(Event):
    id: UUID
    title: str


@dataclass
class ClassifiedAdUpdatedPrice(Event):
    id: UUID
    price: float


@dataclass
class ClassifiedAdRequestedToPublish(Event):
    id: UUID
    published_by: UUID

__all__ = [
    ClassifiedAdCreated,
    ClassifiedAdUpdatedText,
    ClassifiedAdUpdatedTitle,
    ClassifiedAdUpdatedPrice,
    ClassifiedAdRequestedToPublish,
]