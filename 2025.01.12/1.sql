-- 1. Вывести средний оклад (salary) всех сотрудников

select round(avg(salary), 3) avg_salary
from doctors;

------------ 53473.325

-- 2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего (взять явное значение из результата предыдущего запроса)

select round(avg(premium), 3) avg_premium 
from doctors 
where salary > 53473.325;

-- 3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника

select avg(end_date - start_date) days, doctor_id
from vacations
group by doctor_id
order by days;

-- 4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по возрастанию разности между этими двумя значениями

select min(date_part('year', start_date)) min_vacations_year, 
    max(date_part('year', start_date)) max_vacations_year 
from vacations 
group by id 
order by (end_date - start_date);

-- 5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений

select  sum(amount) total_amount
from donations
group by dep_id
order by dep_id;

-- 6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов

select sum(amount) total_year_amount
from donations 
group by sponsor_id, date_part('year', date) 
order by sponsor_id, date_part('year', date);