""" Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split( """

def count_duplicates(string):
    characters = {}
    output = []

    for word in string.split():
        if word in characters:
            characters[word] += 1
            output.append(f"{word}_{characters[word]}")
        else:
            characters[word] = 1
            output.append(word)

    return ' '.join(output)

# Ввод строки пользователем
string = input("Введите строку: ")

# Вызов функции и вывод результата
result = count_duplicates(string)
print(f"Преобразованная строка: {result}")