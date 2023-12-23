from pathlib import Path


def list_files(user_path: str) -> tuple | None:
    """
    Функция возвращает список имен файлов по указанному пути.

    :param user_path: Строка. Абсолютный путь к каталогу.
    :return: Кортеж с именами фалов, если они существуют по указанному пути, иначе None
    """
    path = Path(user_path)
    files = tuple((file.name for file in path.glob('*') if file.is_file()))

    if len(files) > 0:
        return files

