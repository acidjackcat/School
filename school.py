from pupils import Pupil
from Study_class import Class
from personal import Teacher, Director, Stuff


class School(object):
    """Main Parent Class for our school."""

    def __init__(self, name):
        self.name = name
        self.director = []
        self.stuff = []
        self.teachers = []
        self.pupils = []
        self.classes = []

    def assign_class(self, study_class):
        return self.classes.append(study_class)

    def assign_director(self, director):
        self.director.append(director)

    def assign_stuff(self, stuff):
        self.stuff.append(stuff)

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)

    def assign_pupil_to_school(self, pupil):
        return self.pupils.append(pupil)

    @property
    def income(self):
        income = 0
        for classes in self.classes:
            income += classes.outcome
        return income


if __name__ == '__main__':
    academy = School('Academy')
    fifth = Class('Fifth grade', 5)
    academy.assign_class(fifth)
    petrovich = Teacher('Petro', 'Petrovich', 5)
    academy.assign_teacher(petrovich)
    fifth.assign_teacher(petrovich)
    fifth.generate_pupils()
    print(fifth.income)
    print(fifth.outcome)
    print(petrovich.salary)
    print(academy.income)