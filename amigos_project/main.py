from amigos_project.services.utils import change_input
from amigos_project.services.classes import save_to_file


def main():
    """
    Основна логика усього застосунку. Отримуємо ввід від користувача
    і відправляємо його в середину застосунку на обробку.
    :return:
    """
    while True:
        """
            Просимо користувача ввести команду для нашого бота
            Також тут же вимикаємо бота якщо було введено відповідну команду
        """

        user_input = input('Enter command for bot: ')

        result = change_input(user_input)

        print(result)

        if result == 'Good bye!':
            save_to_file()
            break


if __name__ == '__main__':
    main()
