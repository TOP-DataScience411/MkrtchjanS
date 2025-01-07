# Программа проверяет, содержится ли второй список чисел в первом списке.

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for i in range (len(list1)-len(list2)+1):
    if list2 == list1[i:i+len(list2)]:
        print("да")
        break
else:
    print("нет")

#1 2 3 4
#1 2
#да

#1 2 3 4
#2 4
#нет
