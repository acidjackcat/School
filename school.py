from pupils import Pupils
from Study_class import Class
from personal import Teachers, Director, Stuff


class School(object):
    """Main Parent Class for our school."""

    def __init__(self, name):
        self.name = name
        self.director = None
        self.stuff = []
        self.teachers = []
        self.pupils_in_school = []
        self.classes_list = []

    def assign_class(self):
        """Adding study class to school"""
        return self.classes_list.append(Class)

    def assign_director(self):
        self.director = Director()

    def assign_stuff(self):
        self.stuff = Stuff()

    def assign_teacher(self):
        return self.teachers.append(Class.class_teacher)

    def assign_pupils_to_school(self):
        return School.pupils_in_school.append(Class.pupils_in_class)

   # #def debet(self):
   #     """Method for calculation of income and outcome difference."""
  #      debet = len(self.pupils_list)


