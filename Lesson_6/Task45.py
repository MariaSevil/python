""" Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает). """

def get_divisors_sum(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

k = int(input("Введите число k: "))

for i in range(1, k + 1):
    divisors_sum_i = get_divisors_sum(i)
    if divisors_sum_i <= k and divisors_sum_i != i:
        divisors_sum_j = get_divisors_sum(divisors_sum_i)
        if divisors_sum_j == i:
                print(i, divisors_sum_i)
            
