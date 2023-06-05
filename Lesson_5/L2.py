""" Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1 """

def replace_grades(grades):
    max_grade = max(grades)
    min_grade = min(grades)
    replaced_grades = [min_grade if grade == max_grade else grade for grade in grades]
    return replaced_grades

n = int(input("Введите количество оценок: "))
grades = list(map(int, input("Введите оценки через пробел: ").split()))

replaced_grades = replace_grades(grades)
print("Замененные оценки Василия:", ' '.join(map(str, replaced_grades)))

