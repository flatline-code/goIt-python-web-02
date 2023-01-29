from amigos_project.services.utils.sort_files import sort_files
from amigos_project.fabric import *


def stop():
    return 'Good bye!'


def greeting():
    return show_info(ShowCommandsFactory(COMMANDS_INFO))


def handler_sort_files(path: str) -> str:
    return sort_files(path)
