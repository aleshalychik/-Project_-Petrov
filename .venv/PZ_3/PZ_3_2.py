#Единицы длины пронумерованы следующим образом: 1 — дециметр, 2 — километр,
#3 — метр, 4 — миллиметр, 5 — сантиметр. Дан номер единицы длины (целое число
#в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число). Найти
#длину отрезка в метрах.

W = input('Введите длину: ')
L = input('Введите ед. длины, от 1 до 5: ')
while type(W) != int:
  try:
    W = int(W)
  except ValueError:
    print('ошибка')
    W = int(input())
while type(L) != int:
  try:
    L = int(L)
  except ValueError:
    print('ошибка')
    L = int(input('Снова введите ед. длины, от 1 до 5: '))

if 1 <= L <= 5:
  print()
else:
  print('ошибка')
if L == 1:
  print(W * 10)
elif L == 2:
  print(W * 1000)
elif L == 3:
  print(W)
elif L == 4:
  print(W / 1000)
elif L == 5:
  print(W / 10)
else:
  print('ошибка')