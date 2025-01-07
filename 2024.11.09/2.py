# Программа собирает список фруктов, вводимых пользователем, и выводит их в формате, соответствующем количеству введенных фруктов.

fruits = []
    
while True:
    fruit = input()
    if fruit == '':
        break
    fruits.append(fruit)
    
if len(fruits) == 1:
    print(fruits[0])
elif len(fruits) == 2:
    print(f"{fruits[0]} и {fruits[1]}")
else:
    result = ", ".join(fruits[:-1]) + " и " + fruits[-1]
    print(result)
    
#яблоко
#яблоко

#яблоко
#груша
#яблоко и груша

#яблоко
#груша
#апельсин
#яблоко,груша и апельсин
