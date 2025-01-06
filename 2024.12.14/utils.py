from pathlib import Path
from shutil import copyfile

def copy_and_return_path(source_file: Path) -> Path:
    """
    Копирует указанный файл в текущую директорию и возвращает его новый путь.
    """
    target_path = Path.cwd() / "conf.py"
    copyfile(source_file, target_path)
    return target_path