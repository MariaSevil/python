# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)

i = int(input())
j = int(input())

if i > 0 and j > 0:
    total_wagons = i + j - 1
    print(total_wagons)
elif i == 0 or j == 0:
    print("Ошибка: номер вагона не может быть равен нулю.")
elif i < 0 and j < 0:
    total_wagons = abs(i - j) + 1
    print(total_wagons)
else:
    print("Невозможно определить количество вагонов без дополнительной информации.")