select p.* from PERSONA as p 
inner join USUARIO as u on p.idPERSONA=u.PERSONA_idPERSONA
where p.email='antonio@example.com' and p.contraseña=sha('1234');

select p.* from PERSONA as p 
inner join ADMINISTRADOR as a on p.idPERSONA=a.PERSONA_idPERSONA;

select p.* from PERSONA as p 
inner join DOMICILIARIO as d on p.idPERSONA=d.PERSONA_idPERSONA;

delete from USUARIO where PERSONA_idPERSONA='1234';
delete from PERSONA where idPERSONA='1234';

select * from categoria where id=1;
