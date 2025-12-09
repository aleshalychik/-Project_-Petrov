#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов списка с номерами от K до L включительно.

def sum_between_k_and_l(lst, K, L):
    return sum(lst[K-1:L])
print("Пример 1: Ввод данных")
N = (input("Введите размер списка N: "))
while type(N) != int:
  try:
    N = int(N)
  except ValueError:
    print('ошибка')
    N = int(input())
print(f"Введите {N} элементов списка:")
my_list = [int(input(f"Элемент {i+1}: ")) for i in range(N)]
K = (input("Введите число K (1 < K < L < N): "))
while type(K) != int:
  try:
    K = int(K)
  except ValueError:
    print('ошибка')
    K = int(input())
L = (input("Введите число L (1 < K < L < N): "))
while type(L) != int:
  try:
    L = int(L)
  except ValueError:
    print('ошибка')
    L = int(input())
if 1 < K < L < N:
    result = sum_between_k_and_l(my_list, K, L)
    print(f"Сумма элементов с номерами от {K} до {L}: {result}")
else:
    print("Ошибка: нарушены условия 1 < K < L < N")
print("\n" + "="*50 + "\n")
print("Пример 2: Готовые данные")
test_list = [10, 20, 30, 40, 50, 60, 70]
K_test, L_test = 3, 6533

print(f"Список: {test_list}")
print(f"K = {K_test}, L = {L_test}")
print(f"Элементы от K до L: {test_list[K_test-1:L_test]}")
print(f"Их сумма: {sum_between_k_and_l(test_list, K_test, L_test)}")