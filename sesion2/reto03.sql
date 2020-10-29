#¿Cuántos registros hay por cada uno de los puestos?
select nombre, count(*) "Total"
from puesto 
group by nombre;


#¿Cuánto dinero se paga en total por puesto?
select nombre, sum(salario) "Total pagado"
from puesto 
group by nombre;


#¿Cuál es el número total de ventas por vendedor?
select id_empleado, count(clave) "Total de ventas" 
from venta
group by id_empleado order by count(clave) desc;

#¿Cuál es el número total de ventas por artículo?
select id_articulo, count(clave) "Total de ventas" 
from venta
group by id_articulo order by count(clave) desc;
