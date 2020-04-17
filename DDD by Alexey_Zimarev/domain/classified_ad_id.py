from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ClassifiedAdId:
    id: UUID

    def __post_init__(self):
        if not self.id:
            raise ValueError("id must be set")

    def __str__(self) -> str:
        return str(self.id)