#В матрицу найти среднее арифметическое элементов последних двух столбцов

import random
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(3)]

items = [val for row in matrix for val in row[-2:]]

avg = sum(items) / len(items)

for row in matrix: 
  print(row)
print(f"Среднее последних двух столбцов: {avg}")
