#Составить генератор (yield), который преобразует все буквенные символы в заглавные.

def upper(text):
    for char in text:
        if char.isalpha():
            yield char.upper()
        else:
            yield char
s = "абвгдеежзийклмнопрстуфхцчшщъыьэюя"
result = upper(s)
print(list(map(lambda x: x, result)))
