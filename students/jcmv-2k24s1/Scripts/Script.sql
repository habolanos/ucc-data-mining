select count(1) from public.consumos;
select count(1) from public.diasfestivos d ;

select  * from public.diasfestivos d ;

select * from public.consumos;

select c.idproducto , count(1) from public.consumos c group by c.idproducto ;


truncate public.diasfestivos;
truncate public.consumos;
---
UPDATE public.consumos c
   SET c.cantidadfestivos =
       (SELECT d.cantidadmes
          FROM diasfestivos d
         WHERE d.ano = c.anio
           AND d.nmes = c.mes);
           
           
---
UPDATE public.consumos c
   SET cantidadfestivos =
       (SELECT SUM(DISTINCT d.cantidadmes)
          FROM diasfestivos d
         WHERE d.ano = c.anio
           AND d.nmes = c.mes);
