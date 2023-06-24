""" Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод: Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам """

def check_rhythm(poem):
    lines = poem.split()  # Разделяем стихотворение на строки

    syllables_count = None  # Переменная для хранения количества слогов в текущей строке

    for line in lines:
        words = line.split('-')  # Разделяем строку на слова

        current_syllables_count = sum(count_syllables(word) for word in words)  # Вычисляем количество слогов в строке

        if syllables_count is None:  # Если это первая строка, запоминаем количество слогов
            syllables_count = current_syllables_count
        elif current_syllables_count != syllables_count:  # Если количество слогов отличается от предыдущей строки, возвращаем False
            return False

    return True

def count_syllables(word):
    vowels = 'aeiouAEIOU'  # Список гласных букв

    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count

poem = input("Введите стихотворение Винни-Пуха: ")

if check_rhythm(poem):
    print("Парам пам-пам")
else:
    print("Пам парам")