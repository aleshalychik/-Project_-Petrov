#Составить генератор (yield), который преобразует все буквенные символы в заглавные.

import random

# 1. Возрастающая последовательность из n случайных целых чисел, поиск максимума
n = 10
nums = sorted(random.randint(1, 100) for _ in range(n))
print("Возрастающая последовательность:", nums)
print("Максимальный элемент:", max(nums))  # можно просто nums[-1]

# 2. Генератор, переводящий буквы в верхний регистр
def up_gen(s):
    for ch in s:
        yield ch.upper() if ch.isalpha() else ch

# Генерация случайной строки
s = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=15))
print("\nИсходная строка:", s)
print("Результат генератора:", ''.join(up_gen(s)))
