import dataclasses


@dataclasses.dataclass(frozen=True)
class BirdData(object):
    breed: str
    voltage: int
    number_of_coconuts: int

    def asdict(self) -> dict:
        return dataclasses.asdict(self)


class Bird(object):
    def __init__(self, breed: str, voltage: int, number_of_coconuts: int):
        self.breed = breed
        self.voltage = voltage
        self.number_of_coconuts = number_of_coconuts

    def plumage(self) -> str:
        return 'uknown'

    @classmethod
    def create(cls, bird_data: BirdData):
        return {
            'EuropeanSwallow': EuropeanSwallow,
            'AfricanSwallow': AfricanSwallow,
            'NorvegianBlueParrot': NorvegianBlueParrot,
        }.get(bird_data.breed, Bird)(**bird_data.asdict())


class EuropeanSwallow(Bird):
    def plumage(self):
        return 'average'


class AfricanSwallow(Bird):
    def plumage(self):
        return "tired" if self.number_of_coconuts > 2 else "average"


class NorvegianBlueParrot(Bird):
    def plumage(self):
        return "schorched" if self.voltage > 100 else "beatiful"


def plumage(bird_data: BirdData) -> str:
    return Bird.create(bird_data).plumage()


if __name__ == '__main__':
    data = BirdData(breed='NorvegianBlueParrot', voltage=120, number_of_coconuts=3)
    print(plumage(data))

    x = Bird.create(data)
    print(x.plumage())
