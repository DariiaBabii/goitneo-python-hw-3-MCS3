import bot
from address_book import AddressBook

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!\n")

    while True:
        user_input = input("Enter a command: ")
        command, *args = bot.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?\n")
        elif command == "add":
            print(bot.add_contact(args, book))
        elif command == "change":
            print(bot.change_contact(args, book))
        elif command == "phone":
            print(bot.show_phone(args, book))
        elif command == "all":
            print(bot.print_contacts(book))
        elif command == "add-birthday":
            print(bot.add_birthday(args, book))
        elif command == "show-birthday":
            print(bot.show_birthday(args, book))
        elif command == "birthdays":
            print(bot.birthdays(book))
        else:
            print("Invalid command.\n")

if __name__ == "__main__":
    main()