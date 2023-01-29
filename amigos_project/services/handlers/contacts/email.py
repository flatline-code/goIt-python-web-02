from amigos_project.services.decorators import input_error
from amigos_project.services.classes.address_book import ADDRESS_BOOK


@input_error
def add_email(name: str, email: str) -> str:
    if name in ADDRESS_BOOK.keys():
        record = ADDRESS_BOOK.data[name]
        record.add_email(email)

        return f'a new email "{email}" has been added to contact {name}'

    return 'contact does not exist'
