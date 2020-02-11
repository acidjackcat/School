class Pupils(object):
    """Here is the class which should represent students in our school"""
    basic_pay = 100

    def __init__(self, name, surname, year, gender):
        self.f_name = name
        self.l_name = surname
        self.year = year
        self.gender = gender

    def run(self):
        print(f"Я {self.name} {self.surname} бігаю по школі")

    def laugh(self):
        print(f"Я {self.name} {self.surname} сміюсь")

    def learn(self):
        print(f"Я {self.name} {self.surname} вчуся у школі")

    @property
    def pay(self):
        payment = self.basic_pay * self.year
        return payment