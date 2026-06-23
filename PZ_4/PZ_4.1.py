#Дано вещественное число X и целое число N (> 0). Найти значение выражения:
#X - X^3/3! + X^5/5! - ... + (-1)^N * X^(2N+1)/(2N+1)!
#(N! = 1*2*...*N). Полученное число является приближенным значением функции sin в точке X.

import math
X = (input("Введите значение X: "))
N = int(input("Введите целое число N (> 0): "))
while type(X) != float:
  try:
    X = float(X)
  except ValueError:
    print("Неправильно ввели!")
    X = input("Введите первое число: ")
while type(N) != int:
  try:
    N = int(N)
  except ValueError:
    print("Неправильно ввели!")
    N = input("Введите первое число: ")
result = 0
for k in range(1, N + 1):
    exponent = 2 * k - 1
    term = ((-1) ** (k + 1)) * (X ** exponent) / math.factorial(exponent)
    result += term

print("Приближенное значение функции sin:", result)