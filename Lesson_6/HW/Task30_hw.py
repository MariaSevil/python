""" Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: a
n
 = a1
 + (n-1) * d.
Каждое число вводится с новой строки. """

n = int(input("Введите количество элементов: "))
a = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))

progression = []

for i in range(n):
    element = a + i * d
    progression.append(element)

print("Элементы прогрессии:")
for element in progression:
    print(element)
