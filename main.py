from classes import AddressBook, Record
import pickle

def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    cmd = cmd.strip().lower()
    return cmd, *args

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ").strip()
            if not user_input:
                continue

            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                save_data(book)
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                if not args:
                    raise Exception("please enter name")
                elif args and book.find(args[0]):
                    record = book.find(args[0])
                    try:
                        record.add_phone(args[1])
                    except Exception as e:
                        print("Error: ", e)
                else:
                    try:
                        book.add_record(Record(*args))
                    except Exception as e:
                        print("Error: ", e)

            elif command == "change":
                if not args:
                    raise Exception("please enter name")
                elif args and book.find(args[0]):
                    record = book.find(args[0])
                    try:
                        record.edit_phone(args[1], args[2])
                    except Exception as e:
                        print("Error: ", e)
                else:
                    print(f"Record with name {args[0]} not found")

            elif command == "phone":
                if not args:
                    raise Exception("please enter name")
                elif args and book.find(args[0]):
                    record = book.find(args[0])
                    try:
                        print(record.get_phones())
                    except Exception as e:
                        print("Error: ", e)
                else:
                    print(f"Record with name {args[0]} not found")

            elif command == "all":
                for record in book.values():
                    print(record.get_phones())

            elif command == "add-birthday":
                if not args:
                    raise Exception("please enter name")
                elif args and book.find(args[0]):
                    record = book.find(args[0])
                    try:
                        record.add_birthday(args[1])
                    except Exception as e:
                        print("Error: ", e)
                else:
                    print(f"Record with name {args[0]} not found")

            elif command == "show-birthday":
                if not args:
                    raise Exception("please enter name")
                elif args and book.find(args[0]):
                    record = book.find(args[0])
                    try:
                        print(record.get_birthday())
                    except Exception as e:
                        print("Error: ", e)
                else:
                    print(f"Record with name {args[0]} not found")

            elif command == "birthdays":
                print(book.show_records_birthdays())

            else:
                print("Invalid command.")
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()