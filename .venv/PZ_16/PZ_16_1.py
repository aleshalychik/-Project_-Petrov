class Student:
    def __init__(self, first_name, last_name, grades):
        # Инициализация атрибутов
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades  # Список оценок

    def get_average_score(self):
        # Вычисление среднего балла
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        # Студент считается отличником, если его средний балл равен 5.0
        return self.get_average_score() == 5.0

# --- Пример использования ---
student1 = Student("Алексей", "Смирнов", [5, 5, 4, 5])
student2 = Student("Мария", "Иванова", [5, 5, 5, 5])

print(f"Студент: {student1.first_name} {student1.last_name}")
print(f"Средний балл: {student1.get_average_score()}")
print(f"Отличник: {student1.is_excellent()}\n")

print(f"Студент: {student2.first_name} {student2.last_name}")
print(f"Средний балл: {student2.get_average_score()}")
print(f"Отличник: {student2.is_excellent()}")
