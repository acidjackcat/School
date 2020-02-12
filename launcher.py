

if __name__ == '__main__':
    first_year = Excercises.Classroom("first_year", 1)
    first_year.pupils_list = []
    for i in range(30):
        pupil_first = Pupils("First", "Student", 1)
        first_year.pupils_list.append(pupil_first)

    # #def debet(self):
    #     """Method for calculation of income and outcome difference."""
    #      debet = len(self.pupils_list)


    def assign_pupils(self):
        for i in range(int(input('How much pupils are in class:'))):
            pupil = Pupils("Name", "Surname", self.year)
            self.pupils_list.append(pupil)