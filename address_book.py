from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if self.is_valid(value):
            self.value = value
        else:
            raise ValueError("Invalid phone number")

    @staticmethod
    def is_valid(value):
        return value.isdigit() and len(value) == 10

class Birthday(Field):
    def __init__(self, value):
        if not self.confirm(value):
            raise ValueError("Invalid Date of Birth: Value Error")
        self.value = value

    @staticmethod
    def confirm(value):
        today = datetime.today().date()
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y").date()
            if birthday > today:
                return False
        except Exception:
            return False
        return True


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone_number):
        for i, phone in enumerate(self.phones):
            if phone.value == phone_number:
                del self.phones[i]
                return "Phone removed.\n"
        raise ValueError("Phone not found")

    def edit_phone (self, old_number, new_number):
        for i, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[i] = Phone(new_number)
                return "Phone updated.\n"
        raise ValueError("Phone not found")
    
    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
            else:
                raise ValueError("Phone not found")

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return "Birthday added"
    
    def __str__(self):
        return f"Contact name: {self.name.value}, \
        phones: {'; '.join(p.value for p in self.phones)}, \
        birthday: {self.birthday.value if self.birthday else 'Date not added'}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete (self, name):
        if self.find(name):
            del self.data[name]
        else:
            raise ValueError(f"Contact {name} is not exist")


    def get_birthdays_per_week(self):
        working_days = {
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': []
        }

        today = datetime.today().date()
        birthday_info = []
        for name, record in self.data.items():
            if not record.birthday:
                continue
            birthday_obj = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
            birthday_this_year = birthday_obj.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_obj.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                weekday = birthday_this_year.weekday()
                if weekday in [0, 5, 6]:
                    working_days["Monday"].append(name)
                elif weekday == 1:
                    working_days["Tuersday"].append(name)
                elif weekday == 2:
                    working_days["Wednesday"].append(name)
                elif weekday == 3:
                    working_days["Thursday"].append(name)
                elif weekday == 4:
                    working_days["Friday"].append(name)

        for key, value in working_days.items():
            if value != []:
                birthday_info.append(f"\n{key}: {', '.join(value)}\n")
            
        if birthday_info:
            print("Don't forget to wish a happy birthday!")
            return "".join(birthday_info)
        else:
            return "There are no birthdays for this week"



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
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

