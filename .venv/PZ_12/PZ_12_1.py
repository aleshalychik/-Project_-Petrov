import random

# 1. Генерируем матрицу (например, 3 строки и 4 столбца)
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(3)]

# 2. Выбираем все элементы из последних двух столбцов в один список
# row[-2:] — это функциональный срез
items = [val for row in matrix for val in row[-2:]]

# 3. Считаем среднее
avg = sum(items) / len(items)

# Вывод для проверки
for row in matrix: print(row)
print(f"\nСреднее последних двух столбцов: {avg:.2f}")
