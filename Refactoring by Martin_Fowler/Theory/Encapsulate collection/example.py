from dataclasses import dataclass, field
from typing import List


@dataclass
class Course:
    __name: str
    __is_advanced: bool

    @property
    def name(self):
        return self.__name

    @property
    def is_advanced(self):
        return self.__is_advanced


@dataclass
class Person:
    __name: str
    __courses: List[Course] = field(default_factory=list)

    @property
    def name(self):
        return self.__name

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, courses: List[Course]):
        self.__courses = courses


def get_number_of_advanced_courses(person: Person):
    return len([c for c in person.courses if c.is_advanced])


if __name__ == '__main__':
    course1 = Course('Math', True)
    course2 = Course('English', False)
    x = Person("John Wick")
    x.courses = [course1, course2]
    n = get_number_of_advanced_courses(x)
    print(n)
