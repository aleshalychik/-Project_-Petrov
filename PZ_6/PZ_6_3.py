#Дан список размера N, все элементы которого, кроме последнего, упорядочены по возрастанию.
#Сделать список упорядоченным, переместив последний элемент на новую позицию.

def insert_last_element(lst):
    if len(lst) <= 1:
        return lst
    last = lst.pop()
    for i in range(len(lst)):
        if lst[i] > last:
            lst.insert(i, last)
            return lst
    lst.append(last)
    return lst
my_list = [1, 3, 5, 7, 2]
print(f"Исходный список: {my_list}")
result = insert_last_element(my_list)
print(f"Упорядоченный список: {result}")