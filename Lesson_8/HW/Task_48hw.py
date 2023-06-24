""" Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных. """

class Contact:
    def __init__(self, surname, name, patronymic, phone_number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.patronymic}\nНомер телефона: {self.phone_number}\n"

def import_data(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                surname, name, patronymic, phone_number = line.strip().split(',')
                contact = Contact(surname, name, patronymic, phone_number)
                contacts.append(contact)
    except FileNotFoundError:
        print("Файл не найден.")
    return contacts

def export_data(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            line = f"{contact.surname},{contact.name},{contact.patronymic},{contact.phone_number}\n"
            file.write(line)
    print("Данные сохранены в файле.")

def search_contacts(contacts, search_key, search_value):
    search_results = []
    for contact in contacts:
        if getattr(contact, search_key, None) == search_value:
            search_results.append(contact)
    return search_results

def print_contacts(contacts):
    for index, contact in enumerate(contacts, start=1):
        print(f"Контакт {index}:")
        print(contact)

def update_contact(contact, field, value):
    setattr(contact, field, value)
    print("Данные успешно обновлены.")

def delete_contact(contacts, contact):
    contacts.remove(contact)
    print("Контакт успешно удален.")

def main():
    filename = input("Введите имя файла: ")
    contacts = import_data(filename)

    while True:
        print("1. Вывести все контакты")
        print("2. Поиск контакта")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            print_contacts(contacts)
        elif choice == '2':
            search_key = input("Введите характеристику для поиска (например, фамилия): ")
            search_value = input("Введите значение для поиска: ")
            search_results = search_contacts(contacts, search_key, search_value)
            print_contacts(search_results)
        elif choice == '3':
            search_key = input("Введите характеристику для поиска (например, фамилия): ")
            search_value = input("Введите значение для поиска: ")
            search_results = search_contacts(contacts, search_key, search_value)
            if len(search_results) == 0:
                print("Контакт не найден.")
            else:
                print_contacts(search_results)
                contact_index = int(input("Введите номер контакта для изменения: ")) - 1
                if contact_index < 0 or contact_index >= len(search_results):
                    print("Некорректный номер контакта.")
                else:
                    contact = search
                    contact = search_results[contact_index]
                    field = input("Введите поле для изменения (фамилия, имя, отчество, номер): ")
                    value = input("Введите новое значение: ")
                    update_contact(contact, field, value)
                    print("Контакт успешно изменен.")
        elif choice == '4':
            search_key = input("Введите характеристику для поиска (например, фамилия): ")
            search_value = input("Введите значение для поиска: ")
            search_results = search_contacts(contacts, search_key, search_value)
            if len(search_results) == 0:
                print("Контакт не найден.")
            else:
                print_contacts(search_results)
                contact_index = int(input("Введите номер контакта для удаления: ")) - 1
                if contact_index < 0 or contact_index >= len(search_results):
                    print("Некорректный номер контакта.")
                else:
                    contact = search_results[contact_index]
                    delete_contact(contacts, contact)
        elif choice == '5':
            export_data(filename, contacts)
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()