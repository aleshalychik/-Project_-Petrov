#Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и последних строках и столбцах матрицы Matr2 произвольного размера

import random
rows = int(input())
cols = int(input())
Matr2 = [[random.randint(10, 99) for i in range(cols)] for i in range(rows)]

print("Исходная матрица Matr2:")
for r in Matr2: 
  print(r)

Matr1 = [row[1:-1] for row in Matr2[1:-1]]

print("Результат Matr1:")
for r in Matr1: 
  print(r)
