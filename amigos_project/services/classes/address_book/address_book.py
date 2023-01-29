from collections import UserDict
import pickle
import os

from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def search_contacts(self, value: str) -> list[Record] | None:
        found_contacts = []

        for contact in self.data.values():
            if value in contact.name.value or any(value in str(phone.value) for phone in contact.phones):
                found_contacts.append(contact)

        if found_contacts:
            return found_contacts

    @staticmethod
    def load_from_file() -> 'AddressBook':
        filename = "contacts.dat"

        if not os.path.exists(filename):
            return AddressBook()

        with open(filename, 'rb') as file:
            return pickle.load(file)

    def save_to_file(self) -> None:
        filename = "contacts.dat"

        with open(filename, 'wb') as file:
            pickle.dump(self, file)
