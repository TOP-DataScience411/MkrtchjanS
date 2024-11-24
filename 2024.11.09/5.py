scores_letters = {
    1: 'АВЕЁИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
word = input().strip().upper().replace('Ё','Е')

point = {}
for score, letter in scores_letters.items():
    for i in letter:
        point[i] = score
        
count = sum(point.get(i,0) for i in word)

print(count)

#синхрофазотрон
#29