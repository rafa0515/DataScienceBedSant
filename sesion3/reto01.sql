#¿Cuál es el nombre de los empleados cuyo sueldo es menor a $10,000?
select nombre, apellido_paterno from empleado
where id_puesto in (SELECT id_puesto
                    FROM puesto
                    WHERE salario > 10000);
                    
#¿Cuál es la cantidad mínima y máxima de ventas de cada empleado?
select id_empleado, min(total_ventas), max(total_ventas)
from (select clave, id_empleado, count(*) total_ventas
      from venta GROUP BY clave, id_empleado) AS sq group by id_empleado;


#¿Cuáles claves de venta incluyen artículos cuyos precios son mayores a $5,000?
select clave, id_articulo from venta
where id_articulo in (select id_articulo from articulo where precio > 5000);
