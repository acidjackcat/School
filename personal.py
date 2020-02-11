class Personal(object):
    """Main class that represent School personal which should receive salary"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.salary = None


class Teachers(Personal):
    """Simple class to simulate teachers."""

    def __init__(self, name, surname, year):
        super().__init__(name, surname)
        self.year = year
        self.salary = 10000

    def teach(self):
        print(f"I'm {self.name} {self.surname} teaching children.")


class Director(Personal):
    """Class for leading School"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.salary = 20000


class Stuff(Personal):
    """Stuff for cleaning, security, medicine"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.salary = 5000


# Some simple tests
director = Director('Dir', 'One')
print(director.surname, director.salary)

teacher1 = Teachers('vo', 'chan', 2)
print(teacher1.salary, teacher1.year)
