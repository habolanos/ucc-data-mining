select c.idproducto , count(1) from public.consumos c group by c.idproducto ;

-- 
-- select * from public.consumos;

select c.anio , count(1) from public.consumos c where c.idproducto = 1225561 group by c.anio   ;

select * from public.consumos c where c.idproducto = 1225561;

select c.anio , count(1) from public.consumos c group by c.anio;

select * from public.consumos c where c.anio in (2022,2023);


select c.ciclo  from public.consumos c where c.anio in (2022,2023) group by c.ciclo ;

select c.ruta from public.consumos c where c.anio in (2022,2023) group by c.ruta  ;

select *--count(1) 
from public.consumos c where c.anio in (2024) 
and c.barrio = '1 DE MAYO'
limit 1000;

