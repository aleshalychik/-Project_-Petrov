#Составить генератор (yield), который преобразует все буквенные символы в заглавные.

def to_upper_gen(text):
    for char in text:
        if char.isalpha():   # если это буква
            yield char.upper()
        else:
            yield char       # остальные символы без изменений


# пример использования
s = "Hello, мир 123"
result = to_upper_gen(s)

print("".join(result))
