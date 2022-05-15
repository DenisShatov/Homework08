class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.finished_course = []
        self.average_score = 0

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, lectuer, course, grade):
        if isinstance(lectuer, Lecturer) and course in lectuer.courses_attached and course in self.courses_in_progress:
            if course in lectuer.grades and 1 <= grade <= 10:
                lectuer.grades[course] += [grade]
            else:
                lectuer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        self.average_score = sum(map(sum, self.grades.values())) / sum(map(len, self.grades.values()))
        return self.average_score

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
               f'{self.average_rating():0.2f}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if self.average_score < other.average_score:
            print(f'Средняя оценка за домашние задания больше у {other.name}')
        else:
            print(f'Средняя оценка за домашние задания больше у {self.name}')

    def __eq__(self, other):
        if self.average_score == other.average_score:
            return True
        return False

    def __ne__(self, other):
        if self.average_score != other.average_score:
            return True
        return False

    def __gt__(self, other):
        if self.average_score > other.average_score:
            return True
        return False

    def __le__(self, other):
        if self.average_score <= other.average_score:
            return True
        return False

    def __ge__(self, other):
        if self.average_score >= other.average_score:
            return True
        return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_score = 0


class Lecturer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
               f'{Student.average_rating(self):0.2f}'

    def __lt__(self, other):
        if self.average_score < other.average_score:
            print(f'Средняя оценка за лекции больше у {other.name}')
        else:
            print(f'Средняя оценка за лекции больше у {self.name}')

    def __eq__(self, other):
        if self.average_score == other.average_score:
            return True
        return False

    def __ne__(self, other):
        if self.average_score != other.average_score:
            return True
        return False

    def __gt__(self, other):
        if self.average_score > other.average_score:
            return True
        return False

    def __le__(self, other):
        if self.average_score <= other.average_score:
            return True
        return False

    def __ge__(self, other):
        if self.average_score >= other.average_score:
            return True
        return False


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_student(stud, course):
    score = 0
    for obj in stud:
        if course in obj.grades:
            score += sum(obj.grades.get(course)) / len(obj.grades.get(course))
    return f'{(score / len(stud)):0.2f}'


def average_lecturer(lect, course):
    score = 0
    for obj in lect:
        if course in obj.grades:
            score += sum(obj.grades.get(course)) / len(obj.grades.get(course))
    return f'{(score / len(lect)):0.2f}'


# students
first_student = Student('Tanya', 'Ivanova', 'f')
first_student.finished_courses += ['Git', 'Html']
first_student.courses_in_progress += ['Python', 'Go']

second_student = Student('Anton', 'Pavlov', 'm')
second_student.finished_courses += ['Go']
second_student.courses_in_progress += ['Python', 'Git']

# mentors
first_mentor = Mentor('Oksana', 'Petrova')
first_mentor.courses_attached += ['C#']

second_mentor = Mentor('Yriy', 'Dobry')
second_mentor.courses_attached += ['Java']

# reviewers
first_reviewer = Reviewer('Oleg', 'Buldakov')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']

second_reviewer = Reviewer('Ivan', 'Markov')
second_reviewer.courses_attached += ['Go']
second_reviewer.courses_attached += ['Git']

# lecturers
first_lecturer = Lecturer('Ivan', 'Popov')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

second_lecturer = Lecturer('Olga', 'Petrova')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Go']

# grades for students
first_reviewer.rate_student(first_student, 'Python', 9)
first_reviewer.rate_student(first_student, 'Python', 7)
first_reviewer.rate_student(first_student, 'Python', 10)
first_reviewer.rate_student(first_student, 'Git', 10)
first_reviewer.rate_student(first_student, 'Git', 8)
first_reviewer.rate_student(second_student, 'Python', 9)
first_reviewer.rate_student(second_student, 'Python', 7)
first_reviewer.rate_student(second_student, 'Python', 10)
first_reviewer.rate_student(second_student, 'Python', 8)
second_reviewer.rate_student(second_student, 'Git', 9)
second_reviewer.rate_student(second_student, 'Git', 7)
second_reviewer.rate_student(second_student, 'Git', 10)
second_reviewer.rate_student(first_student, 'Go', 10)

# grades for lecturers
first_student.rate_lecturer(first_lecturer, 'Python', 8)
first_student.rate_lecturer(first_lecturer, 'Python', 7)
second_student.rate_lecturer(first_lecturer, 'Git', 10)
second_student.rate_lecturer(first_lecturer, 'Git', 9)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Python', 7)
first_student.rate_lecturer(second_lecturer, 'Python', 6)
first_student.rate_lecturer(second_lecturer, 'Python', 8)
second_student.rate_lecturer(second_lecturer, 'Go', 10)
second_student.rate_lecturer(second_lecturer, 'Go', 9)
first_student.rate_lecturer(second_lecturer, 'Python', 9)
first_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer, 'Go', 8)

# magic metod STR
some_reviewer = first_reviewer.__str__()
print(some_reviewer)

some_lecturer = first_lecturer.__str__()
print(some_lecturer)

some_student = first_student.__str__()
print(some_student)

# comparison
print(first_student < second_student)
print(first_student > second_student)
print(first_student >= second_student)
print(first_student <= second_student)
print(first_student == second_student)
print(first_student != second_student)
print(first_lecturer < second_lecturer)
print(first_lecturer > second_lecturer)
print(first_lecturer >= second_lecturer)
print(first_lecturer <= second_lecturer)
print(first_lecturer == second_lecturer)
print(first_lecturer != second_lecturer)

# field tests
students = [first_student, second_student]
print(f'\nСредняя оценка за домашние задания по всем студентам: {average_student(students, "Python")}')

lecturers = [first_lecturer, second_lecturer]
print(f'\nСредняя оценка за лекции всех лекторов: {average_lecturer(lecturers, "Python")}')
