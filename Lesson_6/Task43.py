""" Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках. """

n = int(input("Введите количество элементов в списке: "))
numbers = []

for _ in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] == numbers[j]:
            count += 1

print("Количество пар элементов, равных друг другу:", count)
