import re

from amigos_project.services.classes.field import Field


class Email(Field):
    @Field.value.setter
    def value(self, value: str):
        self._value = self._check_email(value)

    @staticmethod
    def _check_email(_email: str) -> str:
        if not re.match(r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", _email):
            raise ValueError(f"Invalid email format: {_email}. Email format should be name@domain.com")

        return _email
