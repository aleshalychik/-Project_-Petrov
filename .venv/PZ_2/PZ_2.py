#Дано трехзначное число. В нем зачеркнули первую справа цифру и приписали ее слева. Вывести полученное число.
num = input("Введите трехзначное число: ")
while type(num) != int:
  try:
    num = int(num)
  except ValueError:
    print('ошибка ')
    num = int(input('Снова введите '))
if num < 100 or num > 999:
    print("Ошибка: число должно быть трехзначным ")
else:
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    new_num = units * 100 + hundreds * 10 + tens
    print("Новое число:", new_num)