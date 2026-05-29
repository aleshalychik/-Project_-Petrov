import re

# Исходный HTML-текст задачи (переменная имитирует файл pazzl.html)
html_content = """
<html>
<body bgcolor="#E0FFFF">
<p align="center"><font size="6"><i><b>Р</b></i>азобранный рисунок</font></p>
<table border="2" align="center">
<tr>
<td><img src="majk1.bmp" width="150" height="150"></td>
<td><img src="majk2.bmp" width="150" height="150"></td>
</tr>
<td><img src="majk3.bmp" width="150" height="150"></td>
<td><img src="majk4.bmp" width="150" height="150"></td>
</tr>
</table>
<hr>
<p align="center"><font size="6"><i><b>C</b></i>обранный рисунок</font></p>
<table border="0" align="center" cellpadding="0" cellspacing="0">
<tr>
<td><img src="majk1.bmp" width="150" height="150"></td>
<td><img src="majk2.bmp" width="150" height="150"></td>
</tr>
<td><img src="majk3.bmp" width="150" height="150"></td>
<td><img src="majk4.bmp" width="150" height="150"></td>
</tr>
</table>
</body>
</html>
"""

# Новое, еще более точное регулярное выражение для поиска тегов картинок
# Оно ищет открывающий тег <img, любые символы внутри, и закрывающий тег >
image_pattern = r'<img\s+[^>]*>'

# Находим все теги в тексте
found_images = re.findall(image_pattern, html_content)

# Выводим результаты в консоль PyCharm
print("=== Список найденных HTML-кодов изображений ===")
for index, tag in enumerate(found_images, start=1):
    print(f"{index}. {tag}")

print("-" * 47)
# Считаем количество элементов в списке
print(f"Общее количество найденных изображений: {len(found_images)}")
