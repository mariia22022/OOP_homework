class Student:
    """
    создание экземпляров Student
    методы:
    rate_mentor() реализует добавление оценки преподавателю любым студентом принимает на вход (self,lecturer,course,grade)
    _average_grade(self) расчет средней оценки студента
    __str__(self):
    __lt__(self, other)
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_mentor(self, lecturer, course, grade):
        # выставление оценок преподавателям
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.students_grades:
                lecturer.students_grades[course] += [grade]
            else:
                lecturer.students_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        # реализует  расчет средней оценки по экземпляру класса Student
        for key, value in self.grades.items():
            return round(sum(value) / len(value), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nсредняя оценка за домашние задания: ' \
               f'{self._average_grade()}\nкурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'завершенные курсы: {", ".join(self.finished_courses)}\n'

    def __lt__(self, other):
        # сравнение True/False средних оценок студентов
        if isinstance(other, Student):
            return self._average_grade() < other._average_grade()
        else:
            print("Сравнение некорректно")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """
        создание экземпляров Преподаватель
        методы:
        _average_grade(self) расчет средней оценки преподавателя
        __str__(self):
        __lt__(self, other)
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.students_grades = {}

    def _average_grade(self):
        # расчет средней оценки по экземпляру класса Lecturer
        for key, value in self.students_grades.items():
            return round(sum(value) / len(value), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nсредняя оценка за лекции {self._average_grade()}\n'

    def __lt__(self, other):
        # сравнение True/False средних оценок лекторов
        if isinstance(other, Lecturer):
            return self._average_grade() < other._average_grade()
        else:
            print("Сравнение некорректно")


class Reviewer(Mentor):
    """
          создание экземпляров Проверяющий
          методы:
          rate_hw() реализует добавление оценки студенту проверяющим, принимает на вход (self,lecturer,course,grade)
          __str__(self):
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        # реализует добавление оценки студенту  проверяющим принимает на вход  (self, student, course, grade)
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


student1 = Student('Ruoy', 'Eman')
student1.courses_in_progress += ['Python', 'SQL']
student1.finished_courses += ['Введение в программирование']
print(f'студент1 изучает {student1.courses_in_progress}\n')

student2 = Student('Peter', 'Smirnoff')
student2.courses_in_progress += ['Python', 'SQL']
student2.finished_courses += ['Введение в программирование']
print(f'студент2 изучает {student2.courses_in_progress}\n')

lecturer1 = Lecturer('Dan', 'Smith')
lecturer1.courses_attached = ['Python']
print(f'лектор1 преподает курсы: {lecturer1.courses_attached}\n')

lecturer2 = Lecturer('Serge', 'Levin')
lecturer2.courses_attached = ['SQL']
print(f'лектор2 преподает курсы: {lecturer2.courses_attached}\n')

reviewer1 = Reviewer('Alex', 'Popov')
reviewer1.courses_attached += ['Python', 'SQL']
print(f'курсы проверяющего1 {reviewer1.courses_attached}\n')

reviewer2 = Reviewer('Ivan', 'Ivanov')
reviewer2.courses_attached += ['Python', 'SQL']
print(f'курсы проверяющего2 {reviewer2.courses_attached}\n')


# проверяющий1 ставит оценки студенту1
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'SQL', 10)
# проверяющий1 ставит оценки студенту2
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'SQL', 8)
# проверяющий2 ставит оценки студенту1
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'SQL', 10)
reviewer2.rate_hw(student1, 'SQL', 9)
# проверяющий2 ставит оценки студенту2
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'SQL', 8)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'SQL', 8)


print(f'оценки студента2 {student2.grades}\n')
print(f'оценки студента1 {student1.grades}\n')


# студент1 ставит оценку преподавателю2
student1.rate_mentor(lecturer2, 'SQL', 9)
#  студент1 ставит оценку преподавателю1
student1.rate_mentor(lecturer1, 'Python', 10)
# студент2 ставит оценку преподавателю2
student2.rate_mentor(lecturer2, 'SQL', 10)
# студент2 ставит оценку преподавателю1
student2.rate_mentor(lecturer1, 'Python', 10)
print(f'оценки преподавателя1 {lecturer1.students_grades}\n')
print(f'оценки преподавателя2 {lecturer2.students_grades}\n')

print(student1)
print(student2)
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)

# сравниваем средние оценки студентов используя магический метод __lt__
print(student1 < student2)
print(student1 > student2)

# сравниваем средние оценки преподавателей используя магический метод __lt__
print((lecturer1 > lecturer2))
print(lecturer2 > lecturer1)



def course_average_grades(student_list, course):
    # Функция для подсчета средней оценки за домашние задания  по всем студентам в рамках конкретного курса
    sum_of_grades = 0
    count = 0
    for student in student_list:
        if course in student.courses_in_progress:
            sum_of_grades += sum(student.grades[course])
            count += len(student.grades[course])

    return round(sum_of_grades/count, 2)




def course_average_grades_lecturer(lecturers_list, course):
    # Функция для подсчета средней оценки за лекции по всем преподавателям в рамках конкретного курса
    sum_of_grades = 0
    count = 0
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            sum_of_grades += sum(lecturer.students_grades[course])
            count += len(lecturer.students_grades[course])

    return round(sum_of_grades/count, 2)


course = 'Python'
student_list = [student1, student2]

print(f'средняя оценка студентов на курсе {course} = {course_average_grades(student_list,course)}')

course = 'SQL'
student_list = [student1, student2]
print(f'средняя оценка студентов на курсе {course} = {course_average_grades(student_list,course)}')


course = 'Python'
lecturers_list = [lecturer1, lecturer2]

print(f'средняя оценка преподавателей на курсе {course} = {course_average_grades_lecturer (lecturers_list,course)}')

course = 'SQL'
lecturers_list = [lecturer1, lecturer2]
print(f'средняя оценка преподавателей на курсе {course} ={course_average_grades_lecturer (lecturers_list,course)}')
