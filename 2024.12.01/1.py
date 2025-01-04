from datetime import date, timedelta

def schedule(start_date: date, first_weekday: int, *additional_weekdays: int, total_days: int, date_format: str = '%d/%m/%Y') -> list[str]:
    """
    Создаёт график мероприятий на основе заданных дней недели, исключая каникулы.

    start_date: Дата первого мероприятия.
    first_weekday: Номер первого дня недели (ISO формат: 1 - понедельник, 7 - воскресенье).
    additional_weekdays: Дополнительные дни недели для проведения мероприятий (ISO формат).
    total_days: Общее количество мероприятий.
    date_format: Формат вывода дат (по умолчанию '%d/%m/%Y').
    return: Список строковых представлений дат мероприятий.
    """
    days_to_schedule = set([first_weekday] + list(additional_weekdays))
    excluded_periods = globals().get('vacations', [])

    def valid_dates(start: date):
        current = start
        while True:
            if current.isoweekday() in days_to_schedule:
                if not any(start <= current < (start + duration) for start, duration in excluded_periods):
                    yield current
            current += timedelta(days=1)

    #генерируем расписание
    date_generator = valid_dates(start_date)
    schedule_list = [next(date_generator).strftime(date_format) for _ in range(total_days)]
    
    return schedule_list

# Пример:
#vacations = [(date(2023, 5, 1), timedelta(weeks=1)),(date(2023, 7, 17), timedelta(weeks=1))]
#py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
#print(len(py321)) 
#70
#print(py321[28:32])
#['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']