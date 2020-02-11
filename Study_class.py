from personal import Teachers
from pupils import Pupils
from school import School


class Class(object):

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.pupils_in_class = []
        self.class_teacher = None

    def assign_pupils(self):
        return self.pupils_in_class.append(Pupils)

    def assign_teacher(self):
        self.class_teacher = Teachers()

    @property
    def class_earn(self):
        """Sum of monwy that is bringing separate studdy class"""
        earn = int(Pupils.pay * len(self.pupils_list) - \
                   Teachers.salary)
        return earn
