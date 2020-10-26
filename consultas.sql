select p.* from PERSONA as p 
inner join USUARIO as u on p.idPERSONA=u.PERSONA_idPERSONA
where p.email='antonio@example.com' and p.contraseña=sha('1234');

select p.* from PERSONA as p 
inner join ADMINISTRADOR as a on p.idPERSONA=a.PERSONA_idPERSONA;

select p.* from PERSONA as p 
inner join DOMICILIARIO as d on p.idPERSONA=d.PERSONA_idPERSONA;