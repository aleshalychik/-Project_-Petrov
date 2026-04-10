#Составить генератор (yield), который преобразует все буквенные символы в заглавные.

import random
def uppercase_gen(text):
    transform = lambda ch: ch.upper() if ch.isalpha() else ch
    for k in text:
        yield transform(k)
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
all_chars = letters + digits
print("Исходная строка:", random_text)
print("Результат: ", end="")
for ch in uppercase_gen(random_text):
    print(ch, end="")