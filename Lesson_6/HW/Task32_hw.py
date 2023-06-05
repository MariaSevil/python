""" : Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума) """


def find_indexes(arr, min_value, max_value):
    indexes = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indexes.append(i)
    return indexes

# Пример использования
arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_value = -2
max_value = 4

result = find_indexes(arr, min_value,max_value)
print(result)