-- 1. Вывести названия всех стран Евразии

select name 
from country 
where continent in ('Europe', 'Asia');
 
 -- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет

select region, name
from country
where lifeexpactancy < 50;
 
 -- 3. Вывести название самой крупной по площади страны Африки
 
select name 
from country  
where continent = 'Africa' 
order by surfacearea desc 
limit 1;
   
-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения 

select name 
from country  
where continent = 'Asia' 
order by population / surfacearea
limit 5; 

-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек

select countrycode, name
from city
where population > 5 * 10^6
order by population;

-- 6. Вывести название города в Индии с самым длинным названием

select name 
from city 
order by char_length(name) desc
limit 1;   