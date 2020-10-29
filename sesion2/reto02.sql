#¿Cuál es el promedio de salario de los puestos?
select avg(salario) as "Promedio de salarios"
from puesto;

#¿Cuántos artículos incluyen la palabra Pasta en su nombre?
select count(*) as "Apariciones de pasta"
from articulo where nombre like '%pasta%';

#¿Cuál es el salario mínimo y máximo?
select min(salario) as "Salario mínimo"
from puesto;

#¿Cuál es el salario mínimo y máximo?
select max(salario), min(salario)
from puesto;

#¿Cuál es la suma del salario de los últimos cinco puestos agregados?
select sum(salario) 
from (select * from puesto order by id_puesto desc limit 5) as sub;
