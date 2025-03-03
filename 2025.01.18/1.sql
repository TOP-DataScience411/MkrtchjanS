-- 1. Вывести названия стран и названия сопоставленных им столиц

select c.name country, city.name city 
from country c 
join city on c.capital = city.id;

-- 2. Сравнить по регионам сумму населения стран и сумму населения городов

select c.region, 
        sum(c.population) country_population, 
        sum(city.population) city_population
from country c
join city on c.code = city.countrycode 
group by c.region;

-- 3. Вывести десять языков, на которых разговаривает больше всего людей

select sum(c.population * c.percentage / 100) total_speakers,
        cl.language
from country c 
join countrylanguage cl on c.code = cl.countrycode 
group by cl.language
order by total_speakers desc 
limit 10;
   
-- 4. Вывести названия специальностей и суммарное количество дней отпусков, в которых были врачи каждой специальности; отсортировать по возрастанию суммарного количества дней отпуска

select s.name, 
        sum(end_date - start_date) vacation_days
from specializations s
join doctors_specs d on s.id = d.spec_id
join vacations v on v.doctor_id = d.doctor_id
group by s.name 
order by vacation_days;

-- 5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения (в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; отсортировать по убыванию найденной суммы

select round(sum(amount) / count(name)) amount_ward 
from wards w 
left join donations d on w.dep_id = d.dep_id 
group by w.dep_id 
order by amount_ward  desc;
       