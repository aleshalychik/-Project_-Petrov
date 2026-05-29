import random

# --- 1. ГЕНЕРАЦИЯ И ЗАПИСЬ ИСХОДНЫХ ДАННЫХ ---
# Создаем пустой список и заполняем его 5 случайными числами от -10 до 10
numbers_list = []
for i in range(5):
    random_num = random.randint(-10, 10)
    numbers_list.append(random_num)

# Записываем эти числа в файл через пробел
file = open('numbers.txt', 'w', encoding='utf-8')
for num in numbers_list:
    file.write(str(num) + ' ')
file.close()


# --- 2. ЧТЕНИЕ ИЗ ФАЙЛА И ОБРАБОТКА ---
# Читаем строку из файла
file = open('numbers.txt', 'r', encoding='utf-8')
content = file.read()
file.close()

# Разбиваем строку по пробелам на отдельные элементы-строки
string_elements = content.split()

# Переводим элементы из строк в целые числа с помощью обычного цикла
numbers = []
for item in string_elements:
    numbers.append(int(item))

# Считаем количество и сумму элементов «вручную» через циклы
count = 0
total_sum = 0
for num in numbers:
    count = count + 1
    total_sum = total_sum + num

# Умножаем элементы до n-1 (все, кроме последнего) на элемент n (последний)
processed_elements = []
if count > 0:
    last_element = numbers[count - 1] # Последний элемент списка
    
    # Идем циклом по всем элементам, не доходя до последнего
    for i in range(count - 1):
        multiplied_num = numbers[i] * last_element
        processed_elements.append(multiplied_num)

# Собираем получившиеся числа обратно в строку через пробел
processed_str = ""
for num in processed_elements:
    processed_str = processed_str + str(num) + " "


# --- 3. ЗАПИСЬ РЕЗУЛЬТАТОВ В НОВЫЙ ФАЙЛ ---
file = open('result_numbers.txt', 'w', encoding='utf-8')
file.write("Исходные данные: " + content + "\n")
file.write("Количество элементов: " + str(count) + "\n")
file.write("Сумма элементов: " + str(total_sum) + "\n")
file.write("Элементы до n-1 умножены на элемент n: " + processed_str + "\n")
file.close()

print("Задача 1 успешно выполнена!")
