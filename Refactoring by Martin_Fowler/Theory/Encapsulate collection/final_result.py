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

    def add_course(self, course: Course):
        self.courses.append(course)

    @staticmethod
    def if_not_present():
        raise ValueError('Element not found')

    def remove_course(self, course):
        try:
            self.courses.remove(course)
        except ValueError:
            self.if_not_present()


def get_number_of_advanced_courses(person: Person):
    return len([c for c in person.courses if c.is_advanced])


if __name__ == '__main__':
    course1 = Course('Math', True)
    course2 = Course('English', False)
    x = Person("John Wick")
    x.add_course(course1)
    x.add_course(course2)
    x.add_course(course2)
    x.remove_course(course2)
    n = get_number_of_advanced_courses(x)
    print(n)
