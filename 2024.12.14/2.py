import random
import datetime
from pathlib import Path
from typing import Dict, Literal, Optional

names: Dict[str, Dict[str, list]] = {
    'мужской': {'имя': [], 'отчество': [], 'фамилия': []},
    'женский': {'имя': [], 'отчество': [], 'фамилия': []}
}

def load_data() -> None:
    """
    Загружает данные имен, отчеств и фамилий из файлов в каталог data/names и
    заполняет глобальный словарь names.
    """
    path = Path(r'C:\Users\Svetlana\Desktop\MkrtchjanS\2024.12.14\data\names')
    
    # Загрузка женских имен
    with open(path / 'женские_имена.txt', encoding='utf-8') as f:
        names['женский']['имя'] = [line.strip() for line in f.readlines()]
    
    # Загрузка мужских имен и отчеств
    with open(path / 'мужские_имена_отчества.txt', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                names['мужской']['имя'].append(parts[0])
                names['мужской']['отчество'].append(parts[1].strip('(,)'))
                if len(parts) == 3:
                    names['женский']['отчество'].append(parts[2].strip('()'))
    
    # Загрузка фамилий
    with open(path / 'фамилии.txt', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 2:
                names['мужской']['фамилия'].append(parts[0].strip())
                names['женский']['фамилия'].append(parts[1].strip())
            elif len(parts) == 1:
                surname = parts[0].strip()
                names['мужской']['фамилия'].append(surname)
                names['женский']['фамилия'].append(surname)

def generate_person() -> Dict[str, Optional[str]]:
    """
    Генерирует анкету человека со случайными данными.
    """
    gender = random.choice(['мужской', 'женский'])
    first_name = random.choice(names[gender]['имя'])
    patronymic = random.choice(names[gender]['отчество'])
    last_name = random.choice(names[gender]['фамилия'])
    
    return {
        'имя': first_name,
        'отчество': patronymic,
        'фамилия': last_name,
        'пол': gender,
        'дата рождения': generate_random_date(),
        'мобильный': generate_mobile_number()
    }

def generate_random_date() -> datetime.date:
    """
    Генерирует случайную дату рождения в диапазоне 1923-2023 годов.
    """
    year = random.randint(1923, 2023)
    month = random.randint(1, 12)
    
    # Определяем количество дней в месяце с учетом високосного года
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:  # Февраль
        day = random.randint(1, 29 if is_leap_year(year) else 28)
    
    return datetime.date(year, month, day)

def is_leap_year(year: int) -> bool:
    """
    Проверяет, является ли год високосным.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def generate_mobile_number() -> str:
    """
    Генерирует случайный мобильный номер в формате +79xxxxxxxxx.
    """
    return '+79' + ''.join(random.choices('0123456789', k=9))

load_data()

#from pprint import pprint
#load_data()
#pprint(generate_person(), sort_dicts=False)

#{'имя': 'Эрнест',
#'отчество': 'Созонович',
#'фамилия': 'Римский',
#'пол': 'мужской',
#'дата рождения': datetime.date(1963, 10, 5),
#'мобильный': '+79413733801'}

#{'имя': 'Яна',
#'отчество': 'Аверкиевна',
#'фамилия': 'Пешкова',
#'пол': 'женский',
#'дата рождения': datetime.date(2016, 11, 8),
#'мобильный': '+79786113254'}