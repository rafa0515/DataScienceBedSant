#¿Cuál es el nombre de los empleados que realizaron cada venta?
select clave, nombre, apellido_paterno from venta as v
join empleado as e on v.id_empleado = e.id_empleado
order by clave;

#¿Cuál es el nombre de los artículos que se han vendido?
select clave, nombre from venta as v
join articulo as a on v.id_articulo = a.id_articulo
order by clave;

#¿Cuál es el total de cada venta?
select clave, round(sum(precio),4) as total
from venta as v
join articulo as a on v.id_articulo = a.id_articulo
group by clave order by clave;
