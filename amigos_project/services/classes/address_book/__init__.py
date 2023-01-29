from .address_book import AddressBook
from .record import Record


ADDRESS_BOOK = AddressBook.load_from_file()

__all__ = (
    "ADDRESS_BOOK",
    "Record",
)
