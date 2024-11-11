num =[]

while True:
    a = int(input())
    if a%7 !=0:
        break
    num.append(a)
    
print(" ".join(map(str, reversed(num))))

#Пример ввода:
#7
#7
#14
#21
#13

#Пример вывода: 
#21 14 7 7