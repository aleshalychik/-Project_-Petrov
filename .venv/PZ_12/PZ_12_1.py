#В матрицу найти среднее арифметическое элементов последних двух столбцов

import random

rows = int(input())
cols = int(input())
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
items = [val for row in matrix for val in row[-2:]]

avg = sum(items) / len(items)
print("матрица:")
for row in matrix: 
  print(row)
        
print(f"Среднее последних двух столбцов: {avg}")
