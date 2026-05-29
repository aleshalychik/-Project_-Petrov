import re

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

pattern = r'<img[^>]+>'

image_tags = re.findall(pattern, html_content)

print("Найденные html-коды изображений:")
for tag in image_tags:
    print(tag)

print(f"\nОбщее количество изображений: {len(image_tags)}")
