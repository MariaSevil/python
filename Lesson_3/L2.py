""" Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3 """

list = [1, 2, 3, 4, 5]
n = len(list)
k = 3

k = k % n # если k больше длины последовательности
shifted_list = []
for i in range(n):
    shifted_list.append(list[(i + k) % n])


print(shifted_list)    
    