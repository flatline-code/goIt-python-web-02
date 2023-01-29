class Record:
    def __init__(self,
                 title: list[str] | str,
                 text: str = None,
                 tags: list[str] = None):
        self.title = title if isinstance(title, str) else ' '.join(title)
        self.text = text if text else ''
        self.tags = tags if tags else []

    def change_note(self, title: str) -> str:
        field_for_change = input('enter what do you want to change, title, text or tags of note: ')

        if field_for_change == 'title':
            new_title = input('enter new title: ')

            if self.title == new_title:
                return 'new title must be different, try again'

            self.title = new_title
            return 'note title changed'
        elif field_for_change == 'text':
            self.text = input('enter new text: ')
            return 'note text changed'
        elif field_for_change == 'tags':
            self.tags = input('enter tags: ').split(' ')
            return 'note tags changed'
        else:
            return 'please, type "title" or "text" or "tags" to add changes to note'

    def format_note(self) -> str:
        tags = f'tags: {self.tags}\n' if self.tags else ''

        return (f'title: {self.title}\n'
                f'text: {self.text}\n'
                f'{tags}'
                f'-------------------\n')

    def __repr__(self):
        return f"Record(title={self.title!r}, text={self.text!r}, tags={self.tags!r})"
