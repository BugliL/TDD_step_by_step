from decimal import Decimal
from uuid import UUID


class ClassifiedAd:

    def __init__(self, id: UUID):
        # in the book version here there's a check
        # if (id == default)
        #   throw new ArgumentException( "Identity must be specified", nameof(id));
        # this is not pythonic and I am not checking that the parameter is passed

        # add private things
        self.__id: UUID = id

        self.__ownerId: UUID = None
        self.__title: str = None
        self.__text: str = None
        self.__price: Decimal = None

    @property
    def id(self):
        return self.__id


if __name__ == '__main__':
    import uuid

    x = ClassifiedAd(id=uuid.uuid4())
    print(x.id)
