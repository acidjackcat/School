class Personal(object):
    """Main class that represent School personal which should receive salary"""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.stake = None


class Teacher(Personal):
    """Simple class to simulate teachers."""

    def __init__(self, name, surname, year):
        super().__init__(name, surname)
        self.year = int(year)
        self.stake = 1000

    @property
    def salary(self):
        salary = self.stake * self.year
        return int(salary)


class Director(Personal):
    """Class for leading School"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.stake = 10000

    @property
    def salary(self):
        return self.stake


class Stuff(Personal):
    """Stuff for cleaning, security, medicine"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.stake = 1000

    @property
    def salary(self):
        return self.stake


if __name__ == '__main__':
    director = Director('Dir', 'One')
    print(director.surname, director.salary, director.stake)

    teacher1 = Teacher('vo', 'chan', 2)
    print(teacher1.salary, teacher1.year, teacher1.stake)

    cleaner1 = Stuff('v', 'v')
    print(cleaner1.stake, cleaner1.salary, cleaner1.name)
