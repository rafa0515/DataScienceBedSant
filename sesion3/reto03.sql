# Obtener el puesto de un empleado.
create view Puestos as
select concat(e.nombre, ' ', e.apellido_paterno), p.nombre
from empleado e
join puesto p
  on e.id_puesto = p.id_puesto;
  
select *
from Puestos;


# Saber qué artículos ha vendido cada empleado.
create view empleado_articulo as
select v.clave, concat(e.nombre, ' ', e.apellido_paterno) nombre, a.nombre articulo
from venta v
join empleado e
  on v.id_empleado = e.id_empleado
join articulo a
  on v.id_articulo = a.id_articulo
order by v.clave;

select *
from empleado_articulo;


# Saber qué puesto ha tenido más ventas.
create view puesto_ventas as
select p.nombre, count(v.clave) total
from venta v
join empleado e
  on v.id_empleado = e.id_empleado
join puesto p
  on e.id_puesto = p.id_puesto
group by p.nombre;
select *
from puesto_ventas
order by total desc
limit 1;
