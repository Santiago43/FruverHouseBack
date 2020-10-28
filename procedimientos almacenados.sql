/*Crear usuario*/
delimiter $$

create procedure crearUsuario (
in _cedula varchar(40), 
in _primerNombre varchar(40),
in _segundoNombre varchar(40),
in _primerApellido varchar(40), 
in _segundoApellido varchar(40),
in _direccionResidencia varchar(50),
in _email varchar(60),
in _telefono varchar(15),
in _contraseña varchar(200)
)
begin
insert into PERSONA (idPERSONA,primerNombre,segundoNombre,primerApellido,segundoApellido, direccionResidencia,email,telefono,contraseña) 
values(_cedula,_primerNombre,_segundoNombre,_primerApellido,_segundoApellido,_direccionResidencia,_email,_telefono,sha(_contraseña));
insert into USUARIO (PERSONA_idPERSONA)values (_cedula);
end $$

#drop procedure crearUsuario;