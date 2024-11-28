import datetime

name = input ("Введите имя: ")
surname = input("Введите фамилию: ")
bd_year = int(input("Введите год рождения: "))

age = datetime.datetime.now().year - bd_year

print(surname, name + ',', age)


#Мкртчян Светлана, 21


# ИТОГ: отлично — 4/4

