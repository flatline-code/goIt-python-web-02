import re

from amigos_project.services.classes.field import Field


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        self._value = self.check_phone(value)

    @staticmethod
    def check_phone(phone: str) -> str:
        if not re.fullmatch(r"(^380|0|80)\d{9}$", phone):
            raise ValueError("Invalid, please enter a valid phone number")

        return phone
