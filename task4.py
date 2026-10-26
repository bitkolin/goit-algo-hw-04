def parse_input(user_input):
    """Розбиває введений рядок на команду (в нижньому регістрі) та аргументи."""
    parts = user_input.split()
    if not parts:                       # порожній ввід
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    """Додає контакт: add [ім'я] [телефон]."""
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Змінює номер існуючого контакту: change [ім'я] [новий телефон]."""
    if len(args) != 2:
        return "Usage: change [name] [new phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts):
    """Повертає номер телефону контакту: phone [ім'я]."""
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."


def show_all(contacts):
    """Повертає всі збережені контакти, кожен з нового рядка."""
    if not contacts:
        return "No contacts saved."
    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    """Головний цикл бота: читає команди і виводить відповіді."""
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
            print("Invalid command.")


if __name__ == "__main__":
    main()