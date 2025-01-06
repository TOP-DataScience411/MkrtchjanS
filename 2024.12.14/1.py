from pathlib import Path

def list_files(directory: str):
    """
    Возвращает кортеж с именами файлов в указанном каталоге (нерекурсивно).
    """
    # Создаем объект Path из переданного пути
    path = Path(directory)
    
    # Проверяем, существует ли путь и является ли он каталогом
    if not path.exists() or not path.is_dir():
        return None
    
    # Используем list comprehension для получения всех файлов в каталоге
    files = [file.name for file in path.iterdir() if file.is_file()]
    
    # Возвращаем файлы в виде кортежа
    return tuple(files) if files else None
    
#list_files(r'C:\Users\Svetlana\Desktop\MkrtchjanS\2024.12.14\data')
#('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')
