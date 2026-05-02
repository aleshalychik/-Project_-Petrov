import random

# 1. Генерируем Matr2 произвольного размера (например, 5x6)
rows, cols = 5, 6
Matr2 = [[random.randint(10, 99) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица Matr2:")
for r in Matr2: print(r)

# 2. Переносим элементы (кроме границ) в Matr1
# Matr2[1:-1] — убирает первую и последнюю строки
# row[1:-1] — убирает первый и последний элементы в строке
Matr1 = [row[1:-1] for row in Matr2[1:-1]]

print("\nРезультат Matr1 (внутренняя часть):")
for r in Matr1: print(r)
