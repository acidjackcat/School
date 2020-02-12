class Pupil(object):
    """Here is the class which should represent students in our school"""

    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year
        self.basic_pay = 200

    @property
    def payment(self):
        pay = self.basic_pay * self.year
        return int(pay)


if __name__ == '__main__':
    bob = Pupil("bob", 'rodgers', 5)
    print(bob.basic_pay, bob.name, bob.payment, type(bob.payment))


