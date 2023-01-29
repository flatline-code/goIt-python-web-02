from amigos_project.services.decorators import input_error
from amigos_project.services.classes.notes import NOTES
from amigos_project.services.classes import notes
from amigos_project.fabric import *


@input_error
def add_note(title: str, *args):
    title = title + ' '.join(args) if args else title

    if title in NOTES.keys():
        return 'note with this name already exist'

    while True:
        input_text = input('Enter note text: ')

        if input_text:
            break

    note_tags = input('you can add tags here: ')

    NOTES.add_note(
        notes.Record(title=title, text=input_text, tags=note_tags.split(' ') if note_tags else None)
    )
    return 'new note added'


@input_error
def delete_note(title: str) -> str:
    if title not in NOTES.keys():
        return 'note does not exist'

    NOTES.pop(title)
    return 'note deleted'

# def show_notes() -> str:
#     if not NOTES.keys():
#         return 'nothing to show'

#     all_notes = '-------------------\n'

#     for title, note in NOTES.items():
#         all_notes += note.format_note()

#     return all_notes

def show_notes() -> str:
    return show_info(ShowNotesFactory(NOTES))

# @input_error
# def find_notes(value: str) -> str:
#     if not NOTES.keys():
#         return 'nothing to show'

#     _find_notes = '-------------------\n'

#     for title, note in NOTES.items():
#         if value in title or value in note.text:
#             _find_notes += note.format_note()

#     return _find_notes

@input_error
def find_notes(value: str) -> str:
    return show_info_after_search(ShowNotesFactory(NOTES), value)


@input_error
def change_note(title, *args):
    if args:
        title = title + ' ' + ' '.join(args)
        print(title)
    
    if title not in NOTES.keys():
        return 'note does not exist'

    note = NOTES.data[title]

    result = note.change_note(title)

    NOTES.add_note(note)

    if result == 'note title changed':
        delete_note(title)

    return result


# @input_error
# def find_tag(tag: str) -> str:
#     if not NOTES.keys():
#         return 'nothing to show'

#     filtered_notes: list[notes.Record] = list(filter(lambda x: tag in x.tags, NOTES.values()))
#     filtered_notes.sort()

#     _find_notes = '-------------------\n'

#     for note in filtered_notes:
#         _find_notes += note.format_note()

#     return _find_notes

@input_error
def find_tag(tag: str) -> str:
    return show_info_after_search_by_tag(ShowNotesFactory(NOTES), tag)