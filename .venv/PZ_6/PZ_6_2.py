#Дан целочисленный список размера N. Найти количество различных элементов в данном списке.

def count_unique_elements(lst):
    unique_set = set(lst)
    return len(unique_set)
N = (input("Введите размер списка N: "))
while type(N) != int:
  try:
    N = int(N)
  except ValueError:
    print('ошибка')
    N = int(input())
my_list = [int(input(f"Введите элемент {i+1}: ")) for i in range(N)]
print(f"Исходный список: {my_list}")
print(f"Количество различных элементов: {count_unique_elements(my_list)}")