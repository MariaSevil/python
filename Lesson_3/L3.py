""" Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]  """

list_dictionary =  [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005 "},
    {" V ": " S009 "},
    {" VIII": " S007 "}
]

a = []
for dictionary in list_dictionary:
    for value in dictionary.values():
        value = value.strip()
        a.append(value)

a = set(a)
print(*a)