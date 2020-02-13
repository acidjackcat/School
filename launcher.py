from pupils import Pupil
from Study_class import Class
from personal import Teacher, Director, Stuff
from school import School


"""Launcher for School imitation program"""





academy = School('Academy')
fifth = Class('Fifth grade', 5)
academy.assign_class(fifth)
petrovich = Teacher('Petro', 'Petrovich', 5)
fifth.assign_teacher(petrovich)
fifth.generate_pupils()
print(fifth.income)
print(fifth.outcome)
print(petrovich.salary)
print(academy.debet())