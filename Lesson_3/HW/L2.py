""" Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X """

def find_closest_element(arr, x):
    closest = arr[0]  # Предполагаем, что первый элемент ближайший
    min_diff = abs(arr[0] - x)  # Минимальная разница с первым элементом

    for num in arr:
        diff = abs(num - x)
        if diff < min_diff:
            min_diff = diff
            closest = num

    return closest

# Ввод данных пользователем
N = int(input("Введите количество элементов в массиве: "))
arr = []
for _ in range(N):
    num = int(input("Введите число: "))
    arr.append(num)
x = int(input("Введите число X: "))

# Вызов функции и вывод результата
result = find_closest_element(arr, x)
print(f"Ближайший элемент к числу {x} в массиве: {result}")