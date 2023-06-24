""" 
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной """
class Contact:
    def __init__(self, surname, name, patronymic, phone_number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):
        return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.patronymic}\nНомер телефона: {self.phone_number}\n"

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def import_data(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    surname, name, patronymic, phone_number = line.strip().split(',')
                    contact = Contact(surname, name, patronymic, phone_number)
                    self.contacts.append(contact)
        except FileNotFoundError:
            print("Файл не найден.")

    def export_data(self, filename):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                line = f"{contact.surname},{contact.name},{contact.patronymic},{contact.phone_number}\n"
                file.write(line)
        print("Данные сохранены в файле.")

    def search_contacts(self, search_key, search_value):
        search_results = []
        for contact in self.contacts:
            if getattr(contact, search_key, None) == search_value:
                search_results.append(contact)
        return search_results

    def print_contacts(self):
        for contact in self.contacts:
            print(contact)

def main():
    phonebook = PhoneBook()
    filename = "contacts.txt"
    phonebook.import_data(filename)

    while True:
        print("1. Вывести все контакты")
        print("2. Поиск контакта")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            phonebook.print_contacts()
        elif choice == '2':
            search_key = input("Введите характеристику для поиска (например, фамилия): ")
            search_value = input("Введите значение для поиска: ")
            search_results = phonebook.search_contacts(search_key, search_value)
            phonebook.print_contacts(search_results)
        elif choice == '3':
            phonebook.export_data(filename)
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()