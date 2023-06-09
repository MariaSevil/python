""" Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
 """
# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input("Введите сумму чисел: "))
P = int(input("Введите произведение чисел: "))

X, Y = None, None
found = False

for i in range(1, 1001):
    for j in range(1, 1001):
        if i + j == S and i * j == P:
            X = i
            Y = j
            found = True
            break
    if found:
        break

if found:
    print("Задуманные числа:", X, Y)
else:
    print("Петя дал неверные подсказки.")

