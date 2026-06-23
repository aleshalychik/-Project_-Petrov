#Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами
#(одним или несколькими). Преобразовать каждое слово в строке, заменив в нем все предыдущие вхождения
#его последней буквы на символ «.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «.ИНИ.УМ».
#Количество пробелов между словами не изменять.

def transform_string_simple(s):
    words = s.split(' ')
    result = []
    for word in words:
        if word:
            last = word[-1]
            new_word = word[:-1].replace(last, '.') + last
            result.append(new_word)
        else:
            result.append('')
    return ' '.join(result)
print(transform_string_simple("МИНИМУМ   ПРИВЕТ"))