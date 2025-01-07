def countable_nouns(num: int, forms: tuple[str, str, str]) -> str:
    """Функция возвращает правильную форму существительного в зависимости от числа num."""
    if len(forms) != 3:
        raise ValueError("Кортеж forms должен содержать ровно три элемента.")

    last = num % 10
    last_two = num % 100

    if last_two in (11, 12, 13, 14):
        return forms[2]  
    elif last == 1:
        return forms[0] 
    elif last in (2, 3, 4):
        return forms[1]
    else:
        return forms[2]  

# Примеры ручного тестирования
print(countable_nouns(1, ("год", "года", "лет")))  # 'год'
print(countable_nouns(2, ("год", "года", "лет")))  # 'года'
print(countable_nouns(10, ("год", "года", "лет")))  # 'лет'
print(countable_nouns(12, ("год", "года", "лет")))  # 'лет'
print(countable_nouns(22, ("год", "года", "лет")))  # 'года'
