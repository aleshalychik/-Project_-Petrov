#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Сумма элементов:
#Элементы, умноженные на минимальный элемент:

l = ['-9 6 12 -36 20 45 100 -1']
l2 = []
l3 = []
path1 = 'C:\\Users\\WSR\\PycharmProjects\\PythonProject\\data_3.txt'
path2 = 'C:\\Users\\WSR\\PycharmProjects\\PythonProject\\res.txt'


f3 = open(path1, 'w')
f3.writelines(l)
f3.close()
f4 = open(path1, 'r')
k = f4.read()
f4.close()


for _ in k.split():
    l2.append(int(_))
sm = sum(l2)
mn = min(l2)
for _ in l2:
    l3.append(_ * mn)
f5 = open(path2, 'w')





f5.write('Исходные данные: ' + k + '\n')
f5.write('Количество элементов: ' + str(len(l2)) + '\n')
f5.write('Сумма элементов: ' + str(sm) + '\n')
f5.write('Элементы, умноженные на минимальный элемент: ')



for x in l3:
    f5.write(str(x) + ' ')
f5.close()
