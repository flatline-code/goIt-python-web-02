from datetime import date, timedelta

from amigos_project.services.decorators import input_error
from amigos_project.services.classes.address_book import ADDRESS_BOOK


@input_error
def add_birthday(name: str, birthday: str) -> str:
    if name in ADDRESS_BOOK.keys():
        record = ADDRESS_BOOK.data[name]
        record.add_birthday(birthday)

        return f'birthday {birthday} has been added to contact {name}'

    return 'contact does not exist'


@input_error
def get_birthdays(days: str) -> str:
    try:
        days = int(days)
    except ValueError:
        raise ValueError("You have to enter the days as an even number.")

    day_of_bd = date.today() + timedelta(days)
    list_of_birthdays = ''

    for name, record in ADDRESS_BOOK.items():
        if not record.birthday:
            continue

        birthday = record.birthday.value

        if day_of_bd.month == birthday.month and day_of_bd.day == birthday.day:
            birthday = str(record.birthday.value) if record.birthday else '-'
            list_of_birthdays += f'{record.name.value}: {birthday}\n'

    return list_of_birthdays or "There is no people, who has birthdays on this particular day."
