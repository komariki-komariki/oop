class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def average_value(self):
        _sum = 0
        count = 0
        for courses in self.grades.values():
            for value in courses:
                count += 1
                _sum += value
        return round(_sum / count, 2)

    def __str__(self):
        data_output = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: ' \
                      f'{self.average_value()} \nКурсы в процессе изучения: {",".join(self.courses_in_progress)}' \
                      f'\nЗавершенные курсы: {",".join(self.finished_courses)}'
        return data_output

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не является студентом')
            return
        if self.average_value() > other.average_value():
            print(f'Оценка {self.name} выше оценки {other.name}')
        else:
            print(f'Оценка {self.name} ниже оценки {other.name}')
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}
    def average_value(self):
        _sum = 0
        count = 0
        for courses in self.grades_lecturer.values():
            for value in courses:
                count += 1
                _sum += value
        return round(_sum / count, 2)
    def __str__(self):
        data_output = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка:{self.average_value()}'
        return data_output

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не является лектором')
            return
        if self.average_value() > other.average_value():
            print(f'Оценка {self.name} выше оценки {other.name}')
        else:
            print(f'Оценка {self.name} ниже оценки {other.name}')

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        data_output = f'Имя: {self.name} \nФамилия: {self.surname}'
        return data_output

ruoy_student = Student('Ruoy', 'Eman', 'your_gender')
ruoy_student.courses_in_progress += ['Python', 'HTML']
ruoy_student.finished_courses += ['Git']
nikolay_student = Student('Николай', 'Иванов', 'your_gender')
nikolay_student.courses_in_progress += ['Git', 'Python']
# создали экземпляр класса студент
vasily_lecturer = Lecturer('Василий', 'Петров')
vasily_lecturer.courses_attached += ['Python']
ivan_lecturer = Lecturer('Иван', 'Смирнов')
ivan_lecturer.courses_attached += ['Git', 'Python']
# создали экземпляр класса ревьюер

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
mariya_reviewer = Reviewer('Мария', 'Сидорова')
mariya_reviewer.courses_attached += ['Python', 'Git', 'HTML']
# создали экземпляр класса лектор

some_reviewer.rate_hw(ruoy_student, 'Python', 5)
some_reviewer.rate_hw(ruoy_student, 'Python', 2)
mariya_reviewer.rate_hw(ruoy_student, 'Python', 10)
mariya_reviewer.rate_hw(ruoy_student, 'HTML', 10)
mariya_reviewer.rate_hw(ruoy_student, 'HTML', 10)
mariya_reviewer.rate_hw(ruoy_student, 'HTML', 10)
some_reviewer.rate_hw(nikolay_student, 'Python', 5)
some_reviewer.rate_hw(nikolay_student, 'Python', 2)
mariya_reviewer.rate_hw(nikolay_student, 'Python', 10)
# Оценки выставленные студенту
ruoy_student.rate_lection(vasily_lecturer, 'Python', 1)
ruoy_student.rate_lection(ivan_lecturer, 'Python', 9)
ruoy_student.rate_lection(vasily_lecturer, 'Python', 8)
# Оценки выставленные лектору


# print(vasily_lecturer)
# print('***')
# print(ruoy_student)
# print('***')
# print(mariya_reviewer)
# print('***')
# print('***')
# print(ivan_lecturer)
# print('***')
# print(nikolay_student)
# print('***')
# print(ruoy_student < vasily_lecturer)
# print('***')
# print(ruoy_student < nikolay_student)
# print('***')
# print(ivan_lecturer < vasily_lecturer)
# print('***')
# print(vasily_lecturer < nikolay_student)