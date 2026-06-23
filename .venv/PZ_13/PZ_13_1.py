 Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений.
#Посчитать их количество.

import re
with open('pazzl.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
pattern = r'<img[^>]+>'
image_tags = re.findall(pattern, html_content)
print("Найденные html-коды изображений:")
for tag in image_tags:
    print(tag)
print(f"\nОбщее количество изображений: {len(image_tags)}")
