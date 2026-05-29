# --- ЗАДАЧА 1 ---

# 1. Создаем исходный файл с положительными и отрицательными числами
initial_numbers = [5, -3, 8, -2, 4] 

with open('numbers.txt', 'w', encoding='utf-8') as file:
    # Записываем числа через пробел
    file.write(' '.join(map(str, initial_numbers)))

# 2. Читаем данные из файла для обработки
with open('numbers.txt', 'r', encoding='utf-8') as file:
    content = file.read().strip()
    # Преобразуем строку обратно в список целых чисел
    numbers_list = list(map(int, content.split()))

# Выполняем требуемую обработку
count = len(numbers_list)
total_sum = sum(numbers_list)

# Элементы до n-1 (все кроме последнего) умножаются на элемент n (последний элемент)
if count > 0:
    last_element = numbers_list[-1]
    processed_list = [x * last_element for x in numbers_list[:-1]]
    processed_str = ' '.join(map(str, processed_list))
else:
    processed_str = ""

# 3. Формируем новый текстовый файл с результатами
with open('result_numbers.txt', 'w', encoding='utf-8') as file:
    file.write(f"Исходные данные: {content}\n")
    file.write(f"Количество элементов: {count}\n")
    file.write(f"Сумма элементов: {total_sum}\n")
    file.write(f"Элементы до n-1 умножены на элемент n: {processed_str}\n")

print("Задача 1 выполнена: файл 'result_numbers.txt' успешно сформирован.")
