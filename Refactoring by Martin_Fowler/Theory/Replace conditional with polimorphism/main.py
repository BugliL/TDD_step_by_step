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
        if self.breed == 'EuropeanSwallow':
            return 'average'
        elif self.breed == 'AfricanSwallow':
            return "tired" if self.number_of_coconuts > 2 else "average"
        elif self.breed == 'NorvegianBlueParrot':
            return "schorched" if self.voltage > 100 else "beatiful"
        else:
            return 'uknown'


class EuropeanSwallow(Bird):
    pass


class AfricanSwallow(Bird):
    pass


class NorvegianBlueParrot(Bird):
    pass


def plumage(bird: BirdData) -> str:
    return Bird(**bird.asdict()).plumage()


if __name__ == '__main__':
    data = BirdData(breed='NorvegianBlueParrot', voltage=120, number_of_coconuts=3)
    print(plumage(data))

    x = Bird(**data.asdict())
    print(x.plumage())
