import string

def strong_password(password: str) -> bool:
    """Функция проверяет, является ли переданный пароль надежным."""
    # Пароль считается надежным, если:
    # 1. Его длина не менее 8 символов.
    # 2. Содержит хотя бы одну заглавную букву.
    # 3. Содержит хотя бы одну строчную букву.
    # 4. Содержит как минимум две цифры.
    # 5. Содержит хотя бы один специальный символ или пробел.
    if len(password) < 8:
        return False
    
    upper = any(i.isupper() for i in password)
    lower = any(i.islower() for i in password)
    digit = sum(i.isdigit() for i in password) >= 2
    special = any(i in string.punctuation or i.isspace() for i in password)
    
    return upper and lower and digit and special

# Ручное тестирование
print(strong_password('aP3:kD'))  # False
print(strong_password('aP3:kD_l3'))  # True
print(strong_password('Aa_45_hH_2!'))  # True
print(strong_password('password'))     # False
