from dataclasses import dataclass


@dataclass(frozen=True)
class ClassifiedAdText:
    title: str

    def __post_init__(self):
        if len(self.title) > 300:
            raise ValueError('title must be 300 or less')

    @classmethod
    def create(cls, title: str):
        return cls(title=title)

    def __str__(self):
        return self.title
