def parse_input(user_input):
    """
    Парсить введений користувачем рядок на команду і аргументи.
    """
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def add_contact(args, contacts):
    """
    Додає контакт до словника.
    """
    if len(args) != 2:
        return "Error: You must provide a name and a phone number."

    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."


def change_contact(args, contacts):
    """
    Змінює номер телефону контакту за ім'ям.
    """
    if len(args) != 2:
        return "Error: You must provide a name and a new phone number."

    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact '{name}' updated."
    else:
        return f"Error: Contact '{name}' not found."


def show_phone(args, contacts):
    """
    Показує номер телефону за ім'ям.
    """
    if len(args) != 1:
        return "Error: You must provide a single name."

    name = args[0]
    if name in contacts:
        return f"The phone number for '{name}' is {contacts[name]}."
    else:
        return f"Error: Contact '{name}' not found."


def show_all(contacts):
    """
    Показує всі контакти.
    """
    if not contacts:
        return "No contacts found."
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result


def main():
    """
    Основна функція бота-помічника, яка обробляє команди користувачів.
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
