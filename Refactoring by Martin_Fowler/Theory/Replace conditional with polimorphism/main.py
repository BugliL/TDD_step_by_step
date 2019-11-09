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


def plumage(bird: Bird) -> str:
    return bird.plumage()


if __name__ == '__main__':
    x = Bird(breed='NorvegianBlueParrot', voltage=120, number_of_coconuts=3)
    print(x.plumage())
    print(plumage(x))
