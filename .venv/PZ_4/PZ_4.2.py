#Дано целое число N (> 0). Найти сумму: 1^N + 2^N + ... + N^N

N = (input("Введите целое число N (> 0): "))
while type(N) != int:
  try:
    N = int(N)
  except ValueError:
    print("Неправильно ввели!")
    N = input("Введите первое число: ")
if N <= 0:
    print("N должно быть больше 0.")
else:
    total_sum = 0
    for i in range(1, N + 1):
        t = i * (N - i + 1)
        total_sum += term
    print("Сумма ряда: ", total_sum)