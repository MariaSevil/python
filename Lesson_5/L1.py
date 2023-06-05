""" Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи """

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 0,1
        for _ in range(2, n+1):
            a, b = b, a + b
        return a + b


n = int(input("Введите номер числа Фибоначчи: "))
result = fibonacci(n)
print(f"Число Фибоначчи под номером {n} равно: {result}")