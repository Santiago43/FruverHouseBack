select p.* from PERSONA as p 
inner join USUARIO as u on p.idPERSONA=u.PERSONA_idPERSONA
where p.email='antonio@example.com' and p.contraseña=sha('1234');

select p.* from PERSONA as p 
inner join ADMINISTRADOR as a on p.idPERSONA=a.PERSONA_idPERSONA;

select p.* from PERSONA as p 
inner join DOMICILIARIO as d on p.idPERSONA=d.PERSONA_idPERSONA;

delete from USUARIO where PERSONA_idPERSONA='1234';
delete from PERSONA where idPERSONA='1234';

select * from CATEGORIA where idCATEGORIA=1;

select * from PRODUCTO where idPRODUCTO=1;

select p.nombrePermiso from PERMISO as p 
inner join ADMINISTRADOR_has_PERMISO as ap on p.idPERMISO=ap.PERMISO_idPERMISO
inner join ADMINISTRADOR as a on ap.ADMINISTRADOR_PERSONA_idPERSONA=a.PERSONA_idPERSONA
where a.PERSONA_idPERSONA='12345'