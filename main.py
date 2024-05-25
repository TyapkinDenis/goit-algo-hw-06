from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
           super().__init__(value)
    # реалізація класу

# class Phone(Field):
#     def __init__(self, value):
#            # Phone:Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
#            super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() and len(value) == 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)
    # Phone:Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Реалізовано зберігання об'єкта Name в окремому атрибуті.
    # Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)  

    # Реалізовано методи для додавання 
    # - add_phone/видалення 
    # - remove_phone/редагування 

    def edit_phone(self, phone, new_phone):
        phone_to_edit = self.find_phone(phone)
        if phone_to_edit:
            self.phones.remove(phone_to_edit)
            self.add_phone(new_phone)
    
    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                 return ph
        return

    # - edit_phone/пошуку обєктів Phone - find_phone.

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
          self.data[record.name.value] = record
    # Реалізовано метод add_record, який додає запис до self.data.

    def find(self, name):
        return self.data.get(name, None)
    # Реалізовано метод find, який знаходить запис за ім'ям.

    def delete(self, name):
        if name in self.data:
            del self.data[name]
    # Реалізовано метод delete, який видаляє запис за ім'ям.



# Приклад використання
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone.value}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    # Виведення залишкових записів у книзі
    for name, record in book.data.items():
        print(record)