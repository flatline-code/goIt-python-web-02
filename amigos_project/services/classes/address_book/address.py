from amigos_project.services.classes.field import Field


class Address(Field):
    @Field.value.setter
    def value(self, value):
        self._value = value
