from amigos_project.services.decorators import input_error
from amigos_project.services.classes.address_book import ADDRESS_BOOK
from amigos_project.services.classes import address_book


@input_error
def add_phone(name: str, phone: str) -> str:
    if name in ADDRESS_BOOK.keys():
        record = ADDRESS_BOOK.data[name]
        record.add_phone(phone)

        return f'a new phone "{phone}" has been added to contact {name}'

    return 'contact does not exist'


@input_error
def update_phone(name: str, old_phone: str, new_phone: str) -> str:
    contact: address_book.Record = ADDRESS_BOOK[name]

    updated_phone = contact.update_phone(old_phone, new_phone)

    if updated_phone:
        return f"The old phone {old_phone} was updated to a new one {new_phone}."

    return f"The number {old_phone} of this person was not located in the list."


@input_error
def delete_phone(name: str, phone: str) -> str:
    contact: address_book.Record = ADDRESS_BOOK[name]

    deleted_phone = contact.delete_phone(phone)

    if deleted_phone:
        return f"The phone number {phone} for {name} was removed."

    return f"The number {phone} of this person was not located in the list."
