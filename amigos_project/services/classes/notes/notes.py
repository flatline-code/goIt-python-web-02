from collections import UserDict
import pickle
import os

from .record import Record


class Notes(UserDict):
    def add_note(self, note: Record):
        self.data[note.title] = note

    @staticmethod
    def load_from_file() -> 'Notes':
        filename = "notes.dat"

        if not os.path.exists(filename):
            return Notes()

        with open(filename, 'rb') as file:
            return pickle.load(file)

    def save_to_file(self) -> None:
        filename = "notes.dat"

        with open(filename, 'wb') as file:
            pickle.dump(self, file)
