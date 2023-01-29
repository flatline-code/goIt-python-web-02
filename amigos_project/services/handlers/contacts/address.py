from amigos_project.services.decorators import input_error
from amigos_project.services.classes.address_book import ADDRESS_BOOK
from amigos_project.services.classes import address_book


@input_error
def add_address(name: str, address: str) -> str:
    if name in ADDRESS_BOOK.keys():
        record = ADDRESS_BOOK.data[name]
        record.add_address(address)

        return f'address "{address}" has been added to contact {name}'

    return 'contact does not exist'


@input_error
def update_address(name: str, new_address: str) -> str:
    contact: address_book.Record = ADDRESS_BOOK[name]

    if contact.update_address(new_address):
        return f"The old address was updated to a new one {new_address}."

    return f"The address of this person was not located in the list."


@input_error
def delete_address(name: str) -> str:
    contact: address_book.Record = ADDRESS_BOOK[name]

    contact.address = ''

    return f"The address for {name} was removed."
