class Pupils(object):
    """Here is the class which should represent students in our school"""

    def __init__(self, name, surname, year):
        self.name = name
        self.surname = surname
        self.year = year
        self.basic_pay = 100

    def run(self):
        print(f"Я {self.name} {self.surname} бігаю по школі")

    def laugh(self):
        print(f"Я {self.name} {self.surname} сміюсь")

    def learn(self):
        print(f"Я {self.name} {self.surname} вчуся у школі")

    @property
    def pay(self):
        pay = self.basic_pay * self.year
        return int(pay)


# Some simple tests:
# bob = Pupils("bob", 'rodgers', 5)
# print(bob.basic_pay, bob.name, bob.pay)
