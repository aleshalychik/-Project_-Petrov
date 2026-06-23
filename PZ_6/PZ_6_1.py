#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов списка с номерами от K до L включительно.

def sum_between_k_l(lst, K, L):
    return sum(lst[K-1:L])

# Пример использования
N = 10
K = 3
L = 7
my_list = list(range(1, N+1))

print(f"Список: {my_list}")
print(f"Сумма элементов с {K} по {L}: {sum_between_k_l(my_list, K, L)}")
