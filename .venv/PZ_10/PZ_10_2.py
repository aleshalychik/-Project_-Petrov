# --- 1. ЧТЕНИЕ И ВЫВОД ИСХОДНОГО ТЕКСТА ---
file = open('text18-19.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

print("--- Содержимое файла ---")
print(text)
print("------------------------")


# --- 2. ПОДСЧЕТ БУКВ ЧЕРЕЗ ЦИКЛ ---
letters_count = 0

# Проверяем каждый символ отдельно
for char in text:
    if char.isalpha(): # Если символ является буквой
        letters_count = letters_count + 1

print("Количество символов-букв:", letters_count)


# --- 3. ПЕРЕВОД В НИЖНИЙ РЕГИСТР И ЗАПИСЬ ---
# Метод .lower() переводит весь текст в маленькие буквы
lower_text = text.lower()

file = open('text18-19_lower.txt', 'w', encoding='utf-8')
file.write(lower_text)
file.close()

print("Задача 2 успешно выполнена!")
