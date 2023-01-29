from amigos_project.services.decorators import input_error
from amigos_project.services.classes.address_book import ADDRESS_BOOK
from amigos_project.services.classes import address_book
from amigos_project.fabric import *


@input_error
def add_contact(name: str, phone: str) -> str:
    if name in ADDRESS_BOOK.keys():
        return 'contact already exist'

    ADDRESS_BOOK.add_record(
        address_book.Record(name=name, phone=phone)
    )

    return 'new contact added'


# @input_error
# def find_contacts(value: str) -> str:
#     contacts = ADDRESS_BOOK.search_contacts(value)

#     if not contacts:
#         return "Не знайдено жодного контакта"

#     format_contacts = ""

#     for contact in contacts:
#         format_contacts += contact.format_contact()

#     return format_contacts

@input_error
def find_contacts(value: str) -> str:
    return show_info_after_search(ShowContactsFactory(ADDRESS_BOOK), value)

# def show_all():
#     if not ADDRESS_BOOK:
#         return 'nothing to show'

#     all_contacts = ''

#     for name, record in ADDRESS_BOOK.items():
#         contact_info = f'name: {name}\nphones: {[x.value for x in record.phones]}\n'

#         if record.birthday:
#             contact_info += f'birthday: {record.birthday.value.strftime("%A %d %B %Y")}\n'

#         if record.address:
#             contact_info += f'address: {record.address.value}\n'

#         if record.email:
#             contact_info += f'email: {record.email.value}\n'

#         all_contacts += f'{contact_info}\n'

#     return all_contacts

def show_all():
    return show_info(ShowContactsFactory(ADDRESS_BOOK))

