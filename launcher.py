import school

if __name__ == '__main__':
    first_year = Excercises.Classroom("first_year", 1)
    first_year.pupils_list = []
    for i in range(30):
        pupil_first = Pupils("First", "Student", 1)
        first_year.pupils_list.append(pupil_first)