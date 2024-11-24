import string

def strong_password(password: str) -> bool:
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
