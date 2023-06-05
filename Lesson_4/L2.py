""" Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13 """

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

# Ввод текста пользователем
text = input("Введите текст: ")

# Вызов функции и вывод результата
result = count_unique_words(text)
print(f"Количество различных слов: {result}")