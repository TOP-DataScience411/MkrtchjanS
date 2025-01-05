import csv
from pathlib import Path

class CountableNouns:
    db_path = Path("words.csv")
    words = {} 

    # Чтение базы существительных из файла
    with db_path.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 3:
                words[row[0]] = (row[1], row[2])

    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """Согласование существительного с числом. Если слово отсутствует в базе, вызывает метод save_words.
        """
        if word not in cls.words:
            print(f'существительное "{word}" отсутствует в базе')
            cls.save_words(word1=word)
        
        forms = cls.words[word]
        if 10 < number % 100 < 20 or number % 10 in {0, 5, 6, 7, 8, 9}:
            return forms[1]  
        elif number % 10 == 1:
            return word 
        else:
            return forms[0] 

    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """
        Добавление нового существительного в базу.
        Если слово передано, запрашивает только формы для "два" и "пять".
        """
        if word1:
            word2 = input(f'Введите слово, согласующееся с числительным "два": ').strip()
            word5 = input(f'Введите слово, согласующееся с числительным "пять": ').strip()
            cls.words[word1] = (word2, word5)
        else:
            word1 = input(f'Введите слово, согласующееся с числительным "один": ').strip()
            word2 = input(f'Введите слово, согласующееся с числительным "два": ').strip()
            word5 = input(f'Введите слово, согласующееся с числительным "пять": ').strip()
            cls.words[word1] = (word2, word5)

        # Добавляем запись в файл
        with cls.db_path.open("a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow([word1, cls.words[word1][0], cls.words[word1][1]])
            
            
#CountableNouns.words
#{'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}

#CountableNouns.pick(22, 'год')
#'года'

#CountableNouns.pick(365, 'день')
#'дней'

#CountableNouns.pick(21, 'попугай')
#Введите слово, согласующееся с числительным "два": попугая
#Введите слово, согласующееся с числительным "пять": попугаев

#CountableNouns.words
#{'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}

#CountableNouns.save_words()
#Введите слово, согласующееся с числительным "один": капля
#Введите слово, согласующееся с числительным "два": капли
#Введите слово, согласующееся с числительным "пять": капель

#print(CountableNouns.db_path.read_text(encoding='utf-8'))
#год,года,лет
#месяц,месяца,месяцев
#день,дня,дней
#попугай,попугая,попугаев
#капля,капли,капель

