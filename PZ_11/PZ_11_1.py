#В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.

import random
numbers = list(map(lambda x: random.randint(1, 100), range(9)))
avg = (lambda seq: sum(seq[:3]) / 3)(numbers)
print("Случайные числа:", numbers)
print("Среднее первой трети:", avg)