# --- ЗАДАЧА 2 ---

filename_in = 'text18-19.txt'
filename_out = 'text18-19_lower.txt'

try:
    # 1. Читаем предложенный текстовый файл
    with open(filename_in, 'r', encoding='utf-8') as file:
        text = file.read()

    # 2. Выводим содержимое на экран
    print("\n--- Содержимое файла ---")
    print(text)
    print("------------------------")

    # 3. Считаем количество символов, принадлежащих к группе букв
    letters_count = sum(1 for char in text if char.isalpha())
    print(f"Количество символов-букв: {letters_count}")

    # 4. Формируем новый файл, переводя все символы в нижний регистр
    with open(filename_out, 'w', encoding='utf-8') as file:
        file.write(text.lower())
        
    print(f"Задача 2 выполнена: файл '{filename_out}' успешно создан.")

except FileNotFoundError:
    print(f"\nОшибка: Файл '{filename_in}' не найден. Поместите его в папку со скриптом.")
