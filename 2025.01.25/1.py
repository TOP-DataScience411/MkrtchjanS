import re

month = (
    "январ(?:ь|я)|феврал(?:ь|я)|март?а|"
    "апрел(?:ь|я)|ма[йя]|июн(?:ь|я)|июл(?:ь|я)|"
    "август?а|сентябр(?:ь|я)|октябр(?:ь|я)|"
    "ноябр(?:ь|я)|декабр(?:ь|я)"
)

# Регулярное выражение для диапазона дат в формате "день месяц год – день месяц год"
day_month_year_day_month_year = fr'[1-9]\d? (?:{month}) [12][089][0-9]{{2}} г\.\s*–\s*[1-9]\d? (?:{month}) [12][089][0-9]{{2}} г\.'

with open(r'C:\Users\Svetlana\Homework\15 hw\history_dates_ed.txt', encoding='utf-8') as file:
    text = file.read()

result = re.findall(day_month_year_day_month_year, text, flags=re.MULTILINE)

for res in result:
    print(res)