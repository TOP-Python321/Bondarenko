from utils import important_message


def main() -> None:
    """
    Функция выводит текст сообщения запрошенное от пользователя.
    """
    message = input('Текст сообщения: ')
    print(important_message(message))
