from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
from utils import copy_and_return_path

def request_file() -> object:
    """
    Запрашивает у пользователя путь к файлу и загружает его как модуль.
    """

    while True:
        file_path = input("Введите путь к файлу: ").strip()
        file_to_import = Path(file_path)

        if not file_to_import.exists() or not file_to_import.is_file():
            print("Ошибка: Указанный путь недействителен или файл не существует.")
            continue

        # Используем функцию из utils для копирования файла
        target_file_path = copy_and_return_path(file_to_import)

        # Загружаем модуль из нового файла
        spec = spec_from_file_location("config", target_file_path)
        imported_module = module_from_spec(spec)
        spec.loader.exec_module(imported_module)

        return imported_module
        
#config_module = ask_for_file()
#Введите путь к файлу: d:\student\2023.05.28\conf.py
#Ошибка: Указанный путь недействителен или файл не существует.

#Введите путь к файлу: C:\Users\Svetlana\Desktop\MkrtchjanS\2024.12.14\data\conf.py
#config_module.defaults
#{'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}