from .notes import Notes
from .record import Record


NOTES = Notes.load_from_file()

__all__ = (
    "NOTES",
    "Record",
)
