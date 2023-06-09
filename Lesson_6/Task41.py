""" Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
 """
n = int(input("Введите количество элементов в массиве: "))
array = []

for _ in range(n):
    num = int(input("Введите элемент массива: "))
    array.append(num)

count = 0

for i in range(1, n - 1):
    if array[i] > array[i-1] and array[i] > array[i+1]:
        count += 1

print("Количество элементов, у которых оба соседних элемента меньше данного:", count)