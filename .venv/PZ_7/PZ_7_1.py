#Дана строка. Если она представляет собой запись целого числа, то вывести 1,
#если вещественного (с дробной частью) — вывести 2; если строку нельзя преобразовать
#в число, то вывести 0. Считать, что дробная часть вещественного числа отделяется от
#его целой части десятичной точкой «.».

def check_number_type(s):
    s = s.strip()
    
    if s.replace('.', '', 1).isdigit() and s.count('.') == 1:
        return 2
    elif s.isdigit() or (s.startswith('-') and s[1:].isdigit()):
        return 1
    else:
        return 0
user_input = input("Введите строку: ")
result = check_number_type(user_input)
print(f"Результат: {result}")
