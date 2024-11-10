n1, n2 = input(), input()

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
number = ['1', '2', '3', '4', '5', '6', '7', '8']

if (letter.index(n1[0])+number.index(n1[1]))%2 == (letter.index(n2[0])+number.index(n2[1]))%2:
    print("да")
else: 
    print("нет")

#a1
#b2
#да