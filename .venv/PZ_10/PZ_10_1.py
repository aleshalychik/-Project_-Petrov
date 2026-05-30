# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых
# положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно
#выполнив требуемую обработку элементов:

#Исходные данные:
#Количество элементов:
#Сумма элементов:
#Элементы до n-1 умножены на элемент n:


import random

numbers_list = [random.randint(-10,10)for i in range(5)]

file = open('numbers.txt', 'w', encoding='utf-8')
for num in numbers_list:
    file.write(str(num) + ' ')
file.close()

file = open('numbers.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

string_elements = content.split()

numbers = []
for item in string_elements:
    numbers.append(int(item))

count = 0
total_sum = 0
for num in numbers:
    count = count + 1
    total_sum = total_sum + num

processed_elements = []
if count > 0:
    last_element = numbers[count - 1]

    for i in range(count - 1):
        multiplied_num = numbers[i] * last_element
        processed_elements.append(multiplied_num)

processed_str = ""
for num in processed_elements:
    processed_str = processed_str + str(num) + " "

file = open('result_numbers.txt', 'w', encoding='utf-8')
file.write("Исходные данные: " + content + "\n")
file.write("Количество элементов: " + str(count) + "\n")
file.write("Сумма элементов: " + str(total_sum) + "\n")
file.write("Элементы до n-1 умножены на элемент n: " + processed_str + "\n")
file.close()

print("Задача выполнена")
