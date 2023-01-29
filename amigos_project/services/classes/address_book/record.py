from .name import Name
from .email import Email
from .address import Address
from .phone import Phone
from .birthday import Birthday


class Record:
    def __init__(self,
                 name: str,
                 address: str = None,
                 phone: str = None,
                 email: str = None,
                 birthday: str = None) -> None:
        self.name: Name = Name(name)
        self.address: Address = Address(address) if address else ''
        self.phones: list[Phone] = [Phone(phone)] if phone else []
        self.email: Email = Email(email) if email else ''
        self.birthday: Birthday = Birthday(birthday) if birthday else ''

    def add_address(self, address: str):
        self.address = Address(address)

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def add_email(self, email: str):
        self.email = Email(email)

    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def update_phone(self, old_phone: str, new_phone: str) -> str | None:
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return new_phone

    def delete_phone(self, phone: str) -> str | None:
        for phone_ in self.phones:
            if phone_.value == phone:
                self.phones.remove(phone_)
                return phone

    def update_address(self, address: str) -> Address:
        self.address = Address(address)
        return self.address

    def format_contact(self) -> str:
        phones = [str(x.value) for x in self.phones]
        birthday = self.birthday.value if self.birthday else '-'
        address = self.address.value if self.address else '-'
        email = self.email.value if self.email else '-'

        return f"{self.name.value} : {birthday} : {', '.join(phones)} : {email} : {address}\n"

    def __repr__(self):
        return (
            f"Record(name={self.name!r}, address={self.address!r}, phones={self.phones!r}, birthday={self.birthday!r})"
        )
