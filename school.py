from pupils import Pupils
from personal import Teachers, Director, Stuff
"""Main Class School"""


class School(object):
    """Main Parent Class for our school."""

    def __init__(self, name):
        self.name = name
        director = Director
        stuff = Stuff
        teacher = Teachers

    def debet(self):
        """Method for calculation of income and outcome difference."""
        debet = len(pupils_list)


class Classroom(School):

    def __init__(self, name, year):
        super().__init__(name)
        self.name = name
        self.year = year
        pupils_list = []

    @property
    def class_earn(self):
        earn = Pupils.pay * len(self.pupils_list) - \
               Teachers.salary
        return earn

    @property
    def class_teacher(self):
        class_teacher = School.teacher
