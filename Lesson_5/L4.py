""" Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3 """

def reverse_sequence(sequence):
    reversed_sequence = ""
    for i in range(len(sequence) - 1, -1, -1):
        reversed_sequence += sequence[i]
    return reversed_sequence

n = int(input("Введите количество элементов: "))
sequence = input("Введите последовательность чисел: ")

reversed_sequence = reverse_sequence(sequence)
print(reversed_sequence)