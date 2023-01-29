from amigos_project.services.handlers.common import (
    stop,
    greeting,
    handler_sort_files,
)
from amigos_project.services.handlers.contacts import (
    add_contact,
    find_contacts,
    show_all,
    add_phone,
    update_phone,
    delete_phone,
    add_birthday,
    get_birthdays,
    add_email,
    add_address,
    update_address,
    delete_address,
)
from amigos_project.services.handlers.notes import (
    add_note,
    delete_note,
    show_notes,
    find_notes,
    change_note,
    find_tag,
)

COMMANDS_DICT = {
    'exit': stop,
    'close': stop,
    'hello': greeting,
    'sort_files': handler_sort_files,

    'add_contact': add_contact,
    'find_contacts': find_contacts,
    'show_all': show_all,

    'add_phone': add_phone,
    'update_phone': update_phone,
    'delete_phone': delete_phone,

    'add_birthday': add_birthday,
    'get_birthdays': get_birthdays,
    'add_email': add_email,
    'add_address': add_address,
    'update_address': update_address,
    'delete_address': delete_address,

    'add_note': add_note,
    'delete_note': delete_note,
    'show_notes': show_notes,
    'find_notes': find_notes,
    'change_note': change_note,
    'find_tag': find_tag,
}
