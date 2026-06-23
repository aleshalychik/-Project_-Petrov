#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из результата
#вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль?

def count_steps_to_zero(num):
    steps = 0
    while num > 0:
        digit_sum = sum(int(digit) for digit in str(num))
        num -= digit_sum
        steps += 1
        print(f"Шаг {steps}: число {num + digit_sum} - сумма цифр {digit_sum} = {num}")
    return steps
number = (input("Введите число: "))
while type(number) != int:
  try:
    number = float(number)
  except ValueError:
    print("Неправильно ввели!")
    number = input("Введите первое число: ")
result = count_steps_to_zero(number)
print(f"Количество действий до нуля: {result}")