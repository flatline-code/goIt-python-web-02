from datetime import datetime

from amigos_project.services.classes.field import Field


class Birthday(Field):
    @Field.value.setter
    def value(self, value: str):
        try:
            self._value = datetime.strptime(value, '%d.%m.%Y')

        except (ValueError, TypeError):
            raise ValueError("Invalid. Enter date in format DD.MM.YYYY")
