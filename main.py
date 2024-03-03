from classes import AddressBook, Record

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if not args:
                raise Exception('please enter name')
            elif args and book.find(args[0]):
                record = book.find(args[0])
                try:
                    record.add_phone(args[1])
                except Exception as e:
                    print("Error Occured, plese make sure to pass phone number as second argument: ", e)        
            else:    
                book.add_record(Record(*args))

        elif command == "change":
            if not args:
                raise Exception('please enter name')
            elif args and book.find(args[0]):
                record = book.find(args[0])
                try:
                    record.edit_phone(args[1], args[2])
                except Exception as e:
                    print("Error Occured, plese make sure to pass phone number to edit and new value: ", e)        
            else:    
                print(f"Record with name {args[0]} not found")

        elif command == "phone":
            if not args:
                raise Exception('please enter name')
            elif args and book.find(args[0]):
                record = book.find(args[0])
                try:
                    print(record.get_phones())
                except Exception as e:
                    print("Error Occured: ", e)        
            else:    
                print(f"Record with name {args[0]} not found")

        elif command == "all":
            print(book)

        elif command == "add-birthday":
            if not args:
                raise Exception('please enter name')
            elif args and book.find(args[0]):
                record = book.find(args[0])
                try:
                    record.add_birthday(args[1])
                except Exception as e:
                    print("Error Occured, make sure passing the date: ", e)        
            else:    
                print(f"Record with name {args[0]} not found")

        elif command == "show-birthday":
            if not args:
                raise Exception('please enter name')
            elif args and book.find(args[0]):
                record = book.find(args[0])
                try:
                    print(record.get_birthday())
                except Exception as e:
                    print("Error Occured, make sure passing the date: ", e)        
            else:    
                print(f"Record with name {args[0]} not found")

        elif command == "birthdays":
            print(book.show_records_birthdays())

        else:
            print("Invalid command.")

if __name__ == '__main__':     
    main()