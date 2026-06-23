#Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
#Добавьте методы для вычисления среднего балла и определения, является ли студент
#отличником


import random

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades
    def get_average_score(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return self.get_average_score() == 5.0

random_grades_1 = [random.randint(2, 5) for _ in range(random.randint(3, 7))]
random_grades_2 = [random.randint(4, 5) for _ in range(random.randint(3, 5))]

student1 = Student("Алексей", "Смирнов", random_grades_1)
student2 = Student("Мария", "Иванова", random_grades_2)

print(f"Студент: {student1.first_name} {student1.last_name}")
print(f"Случайные оценки: {student1.grades}")
print(f"Средний балл: {student1.get_average_score():.2f}")
print(f"Отличник: {student1.is_excellent()}\n")

print(f"Студент: {student2.first_name} {student2.last_name}")
print(f"Случайные оценки: {student2.grades}")
print(f"Средний балл: {student2.get_average_score():.2f}")
print(f"Отличник: {student2.is_excellent()}")
