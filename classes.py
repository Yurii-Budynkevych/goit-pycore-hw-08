from collections import UserDict
from datetime import datetime
import re

class PhoneError(Exception):
    def __init__(self, message="not ok number"):
        self.message = message
        super().__init__(self.message)

class Field:
    def __init__(self, value):
        self.value = value
        
    def get_value (self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        name = name.lower().capitalize() 
        super().__init__(name)    

class Phone(Field):
    __pattern = r"^\+?\d{10,}$"

    def __init__(self, phone):
        if not phone:
                raise PhoneError("Plese enter phone")
        elif not re.match(self.__pattern, phone):
                raise PhoneError() 
        super().__init__(phone)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")    

    def __repr__(self):
        return f"Object Birthday. birthday: {self.date}"


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone)]
        self.birthday = birthday
  
    def add_phone (self, phone):
        new_phone = Phone(phone) 
        self.phones.append(new_phone)

    def edit_phone (self, phone, edited_phone):
        for el in self.phones:
            if el.value == phone:
                el.value = edited_phone

    def find_phone (self, phone):
        for el in self.phones:
            if el.value == phone:
                return phone
        return 'not found'
    
    def get_phones (self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_birthday (self, birthday):
        new_birthday = Birthday(birthday) 
        self.birthday = new_birthday

    def get_birthday (self):
        return f"Contact name: {self.name.value}, birthday: {self.birthday}"
    
    def __repr__ (self):
        return f"Object Record. phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.get_value()] = record

    def find(self, record_name):
        return self.data.get(record_name)
    
    def show_records_birthdays(self):
        birthday_list = []
        for record_name, record in self.data.items():
            if record.birthday:
                birthday_list.append((record_name, record.get_birthday()))
        return birthday_list

    def delete(self, record_name):
        self.data.pop(record_name) 

