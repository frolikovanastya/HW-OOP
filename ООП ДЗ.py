class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
   
    def am_rate(self):
        sum_1 = 0
        len_1 = 0
        for i in self.grades.values():
            sum_1 += sum(i)
            len_1 += len(i)
        result = round(sum_1 / len_1, 2)
        return result

    def am_rate_course(self, course):
        sum_2 = 0
        len_2 = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_2 += sum(self.grades[course])
                len_2 += len(self.grades[course])
        average_rating = round(sum_2 / len_2, 2)
        return average_rating               

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.am_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Лекторов и учеников сравнивать нельзя")
            return
        return self.am_rate() < other.am_rate()




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def am_rate(self):
        sum_3 = 0
        len_3 = 0
        for crs in self.grades.values():
            sum_3 += sum(crs)
            len_3 += len(crs)
        result = round(sum_3 / len_3, 2)
        return result

    def am_rate_course(self, course):
        sum_2 = 0
        len_2 = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_2 += sum(self.grades[course])
                len_2 += len(self.grades[course])
        average_rating = round(sum_2 / len_2, 2)
        return average_rating

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.am_rate()}"
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Лекторов и учеников сравнивать ньльзя")
            return
        return self.am_rate() < other.am_rate()      




class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        result = f'Имя: {self.name} \nФамилия: {self.surname}'
        return result

student_1 = Student('Синицина', 'Дарья', 'жен')
student_1.courses_in_progress += ["Python", "Java"]
student_1.finished_courses += ["C++"]
student_2 = Student('Ксения', 'Котова', 'Жен')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Java"]

lecturer_1 = Lecturer("Сергей", 'Орлов')
lecturer_1.courses_attached += ['Python', "C++", "Java"]
lecturer_2 = Lecturer('Животова', 'Елена')
lecturer_2.courses_attached += ['Python', "C++"]

reviewer_1 = Reviewer('Анна', 'Капранова')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Ольга', 'Ольгова')
reviewer_2.courses_attached += ['Python', "Java"]

reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 5)

student_1.rate_lecture(lecturer_1, 'Python', 3)
student_1.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_1, 'Python', 5)
student_2.rate_lecture(lecturer_2, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Python', 2)
student_2.rate_lecture(lecturer_2, 'Python', 10)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

def am_rate_all_course_std(course, student_list):
    sum_4 = 0
    qtty = 0
    for i in student_list:
        for crs in i.grades:
            std_sum_rate = i.am_rate_course(course)
            sum_4 += std_sum_rate
            qtty += 1
    result = round(sum_4 / qtty, 2)
    return result


def am_rate_all_course_lct(course, lecturer_list):
    sum_5 = 0
    qty_5 = 0
    for l in lecturer_list:
        for c in l.grades:
            lct_sum = l.am_rate_course(course)
            sum_5 += lct_sum
            qty_5 += 1
    result = round(sum_5 / qty_5, 2)
    return result
print("Средняя оценка за курс у всех студентов:")
print(am_rate_all_course_std('Python', student_list))
print("Средняя оценка за курс у всех лекторов:")
print(am_rate_all_course_lct('Python', lecturer_list))
print()
print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(lecturer_2)





