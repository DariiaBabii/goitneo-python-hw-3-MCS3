from address_book import Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone with 10 values please.\n"
        except IndexError:
            return "Index out of bounds or does not exist"
        except KeyError as ke:
            return f"This contact {ke} does not exist"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    name, phone = args
    contact = book.find(name)
    if contact:
        contact.add_phone(phone)
        return "Contact already exists.\n"
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added.\n"

@input_error
def change_contact(args, book):
    name, old_number, new_number = args
    if name not in book.find(name):
        return "Contact not found.\n"
    else:
        contact = book.find(name)
        contact.edit_phone(old_number, new_number)
        return "Contact updated.\n"

@input_error
def show_phone(args, book):
    name = args[0]
    contact = book.find(name)
    if contact not in book:
        return f"Contact {name} not found.\n"
    else:
        return contact

@input_error
def print_contacts(book):
    contact_list = []
    if not book.data:
        return "No contacts.\n"
    for name, phone in book.data.items():
        contact_list.append(f"\n{name}: {phone}\n")
    return "".join(contact_list)

@input_error
def add_birthday(args, book):
    name = args[0]
    birthday = args[1]
    contact = book.find(name)
    if contact:
        contact.add_birthday(birthday)
        return "Birthday added"
    else:
        return f"Contact: {name} not found!"


@input_error
def show_birthday(args, book):
    name = args[0]
    contact = book.find(name)
    if contact and contact.birthday:
        return contact.birthday.value
    else:
        return "Birthday not found."


@input_error
def birthdays(book):
    return book.get_birthdays_per_week()


if __name__ == "__main__":
    print("Welcome to the assistant function!")