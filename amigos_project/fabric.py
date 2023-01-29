from abc import ABC, abstractmethod
from amigos_project.services.classes.address_book import ADDRESS_BOOK
from amigos_project.services.classes.notes import NOTES


# опис команд буде більш інформативний
COMMANDS_INFO = {
    'hello': 'показати всі доступні команди',
    'exit': 'вихід з програми',
    'close': 'вихід з програми',
    'sort_files': 'відсортувати файли',

    'add_contact': 'додати контакт',
    'find_contacts': 'знайти контакт',
    'show_all': 'показати всі контакти',

    'add_phone': 'додати номер телефону до контакту',
    'update_phone': 'оновити номер телефон',
    'delete_phone': 'видалити номер телефону',

    'add_birthday': 'додати день народження до контакту',
    'get_birthdays': 'отримати контакти, у котрих день народження у вказану дату',
    'add_email': 'додати email до контакту',
    'add_address': 'додати адресу до контакту',
    'update_address': 'оновити адресу контакта',
    'delete_address': 'видалити адресу у контакта',

    'add_note': 'додати замітку',
    'delete_note': 'видалити замітку',
    'show_notes': 'показати всі замітки',
    'find_notes': 'знайти замітки',
    'change_note': 'змінити замітку',
    'find_tag': 'знайти замітку за тегом',
}

class Operation(ABC):
    
    @abstractmethod
    def show_all_records(self):
        pass

    @abstractmethod
    def show_records_after_search(self, search_words):
        pass

class ShowContacts(Operation):
    def __init__(self, data: dict):
        super().__init__()
        self.data = data.values()

    def show_all_records(self, list_of_records = None) -> str:
        if not self.data:
            return 'nothing to show'

        records = list_of_records if list_of_records else self.data

        all_records = ''

        for record in records:
            contact_info = f'name: {record.name.value}\nphones: {[x.value for x in record.phones]}\n'

            if record.birthday:
                contact_info += f'birthday: {record.birthday.value.strftime("%A %d %B %Y")}\n'

            if record.address:
                contact_info += f'address: {record.address.value}\n'

            if record.email:
                contact_info += f'email: {record.email.value}\n'

            all_records += f'{contact_info}\n'

        return all_records 

    def show_records_after_search(self, search_words: str) -> str:
        if not self.data:
            return 'nothing to show'
        
        found_records = []

        for record in self.data:
            if search_words in record.name.value or any(search_words in srt(phone.value) for phone in record.phones):
                found_records.append(record)

        return self.show_all_records(found_records) if found_records else 'no matches'

class ShowNotes(Operation):
    def __init__(self, data: dict):    
        super().__init__()
        self.data = data.values()
        
    def show_all_records(self, list_of_records = None) -> str:
        if not self.data:
            return 'nothing to show'
        
        records = list_of_records if list_of_records else self.data

        all_records = '-------------------\n'

        for record in records:
            tags = f'tags: {record.tags}\n' if record.tags else ''

            note_info = (f'title: {record.title}\n'
                         f'text: {record.text}\n'
                         f'{tags}'
                         f'-------------------\n')

            all_records += f'{note_info}\n'

        return all_records

    def show_records_after_search(self, search_words: str) -> str:
        if not self.data:
            return 'nothing to show'

        found_records = []

        for record in self.data:
            if search_words in record.title or search_words in record.text:
                found_records.append(record)

        return self.show_all_records(found_records) if found_records else 'no matches'

    def show_records_by_tag(self, tag: str) -> str:
        if not self.data:
            return 'nothing to show'

        found_records = []

        for record in self.data:
            if tag in record.tags:
                found_records.append(record)

        return self.show_all_records(found_records) if found_records else 'no matches'

class ShowCommands(Operation):
    def __init__(self, data: dict):    
        super().__init__()
        self.data = data

    def show_all_records(self):
        all_commands = '-------------------\n'

        for command, info in self.data.items():
            command_info = (f'{command}: {info}\n'
                            f'-------------------\n')

            all_commands += f'{command_info}\n'

        return all_commands

    def show_records_after_search(self, search_words):
        pass
            

class Factory(ABC):
    @abstractmethod
    def create_operation(self) -> Operation:
        pass

    def make_operation(self) -> Operation:
        return self.create_operation()

class ShowContactsFactory(Factory):
    def __init__(self, data: dict):
        self.data = data

    def create_operation(self) -> Operation:
        return ShowContacts(self.data)

class ShowNotesFactory(Factory):
    def __init__(self, data: dict):
        self.data = data

    def create_operation(self) -> Operation:
        return ShowNotes(self.data)

class ShowCommandsFactory(Factory):
    def __init__(self, data: dict):
        self.data = data

    def create_operation(self) -> Operation:
        return ShowCommands(self.data)

def show_info(factory: Factory):
    operator = factory.make_operation()
    return operator.show_all_records()

def show_info_after_search(factory: Factory, words: str) -> str:
    operator = factory.make_operation()
    return operator.show_records_after_search(words)

def show_info_after_search_by_tag(factory: Factory, tag: str) -> str: 
    operator = factory.make_operation()
    return operator.show_records_by_tag(tag)

if __name__ == '__main__':
    print(show_info(ShowCommandsFactory(COMMANDS_INFO)))