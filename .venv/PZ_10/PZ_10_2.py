#Из предложенного текстового файла (text18-19.txt) вывести на экран его содержимое, количество символов,
#принадлежащих к группе букв. Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно заменив символы верхнего регистра на нижний.


file = open('text18-19.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

print("--- Содержимое файла ---")
print(text)

letters_count = 0

for char in text:
    if char.isalpha():
        letters_count = letters_count + 1

print("Количество символов-букв:", letters_count)

lower_text = text.lower()

file = open('text18-19_lower.txt', 'w', encoding='utf-8')
file.write(lower_text)
file.close()

print("Задача выполнена")
