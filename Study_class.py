from personal import Teacher
from pupils import Pupil


class Class(object):

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.pupils = []
        self.teachers = []

    def assign_pupil(self, pupil):
        self.pupils.append(pupil)

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)

    @property
    def income(self):
        income = 0
        for pupil in self.pupils:
            income += pupil.payment
        return income

    @property
    def outcome(self):
        outcome = 0
        for teacher in self.teachers:
            outcome += teacher.salary
        return self.income - outcome

    def generate_pupils(self):
        for i in range(int(input('How much pupils are in class:'))):
            pupil = Pupil("Name", "Surname", self.year)
            self.pupils.append(pupil)


if __name__ == '__main__':
    fifth = Class('Fifth grade', 5)
    petrovich = Teacher('Petro', 'Petrovich', 5)
    fifth.assign_teacher(petrovich)
    vasia = Pupil('vasia', 'pupkin', 5)
    fifth.assign_pupil(vasia)
    fifth.generate_pupils()
    print(f"Class iscome is {fifth.income}")
    print(fifth.outcome)
    print(petrovich.salary)