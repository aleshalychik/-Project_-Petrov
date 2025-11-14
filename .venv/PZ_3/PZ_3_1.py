#Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел
#А и В нечетное».

A = input('Введите число')
B = input('Введите число')
while type(A) != int:
  try:
    A = int(A)
  except ValueError:
    print('ошибка')
    A = int(input('Снова введите'))
while type(B) != int:
  try:
    B = int(B)
  except ValueError:
    print('ошибка')
    B = int(input('Снова введите'))
if A % 2 != 0 and B % 2 != 0:
  print('истинно')
else:
  print('ложно')