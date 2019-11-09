class Bird(object):
    def __init__(self, breed: str, voltage: int, number_of_coconuts: int):
        self.breed = breed
        self.voltage = voltage
        self.number_of_coconuts = number_of_coconuts


def plumage(bird: Bird) -> str:
    if bird.breed == 'EuropeanSwallow':
        return 'average'
    elif bird.breed == 'AfricanSwallow':
        return "tired" if bird.number_of_coconuts > 2 else "average"
    elif bird.breed == 'NorvegianBlueParrot':
        return "schorched" if bird.voltage > 100 else "beatiful"
    else:
        return 'uknown'
