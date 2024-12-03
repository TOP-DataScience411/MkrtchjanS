def deck ():
    masties = ['черви', 'бубны', 'пики', 'трефы']
    ranks = list(range(2,11))+['валет', 'дама', 'король','туз']
    for masti in masties:
        for rank in ranks:
            yield (rank, masti)

print(list(deck())[::13])
#[(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]