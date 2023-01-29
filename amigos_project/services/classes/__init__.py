from .notes import NOTES
from .address_book import ADDRESS_BOOK


def save_to_file() -> None:
    ADDRESS_BOOK.save_to_file()
    NOTES.save_to_file()


__all__ = (
    "save_to_file",
)
