

def same_by(characteristic, objects):
    if not objects:  # Проверяем пустой ли список объектов
        return True

    first_value = characteristic(objects[0])  # Вычисляем характеристику для первого объекта

    for obj in objects[1:]:
        if characteristic(obj) != first_value:
            return False

    return True

values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')