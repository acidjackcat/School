from personal import Teachers
from pupils import Pupils



class Class(object):

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.pupils_list = []
        self.teachers_list = []

    def assign_pupil(self, pupil):
        return self.pupils_list.append(pupil)

    def assign_teacher(self, teacher):
        return self.teachers_list.append(teacher)

    def class_earn(self):
        earn = 0
        for pupil in self.pupils_list:
            earn += pupil.payment()
        return earn


if __name__ == '__main__':
    fifth = Class('Fifth grade', 5)
    fifth.assign_pupil()
    fifth.class_earn()