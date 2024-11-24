a = input().strip()
binary = {'0', '1'}

if a.startswith('0b'):
    a = a[2:]
elif a.startswith('b'):
    a = a[1:]
    
for i in a[0:]: 
    if i not in binary:
        print("нет")
        exit()

print("да")

#1b0101
#нет

