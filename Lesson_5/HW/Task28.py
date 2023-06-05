""" Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы. """

def sum_recursive(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum_recursive(a + 1, b - 1)
    else:
        return sum_recursive(a - 1, b + 1)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = sum_recursive(a, b)
print(f"Сумма чисел {a} и {b} равна {result}")

