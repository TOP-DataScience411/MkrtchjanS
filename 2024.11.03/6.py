a = input()

if len(a) != 6:
    print("Некорректный номер билета")
else:
    half1 = a[:3]
    half2 = a[3:]
    sum_half1 = sum(int(i) for i in half1)
    sum_half2 = sum(int(i) for i in half2)

    if sum_half1 == sum_half2:
        print('да')
    else: 
        print('нет')

#183534
#да

#401367
#нет
