/*Crear usuario*/
delimiter $$

create procedure crearUsuario (
in _documento varchar(40), 
in _tipoDocumento int,
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
insert into PERSONA (idPERSONA,tipoDocumento,primerNombre,segundoNombre,primerApellido,segundoApellido, direccionResidencia,email,telefono,contraseña) 
values(_documento,_tipoDocumento,_primerNombre,_segundoNombre,_primerApellido,_segundoApellido,_direccionResidencia,_email,_telefono,sha(_contraseña));
insert into USUARIO (PERSONA_idPERSONA)values (_documento);
end $$
#drop procedure crearUsuario;


/*Crear admin*/
delimiter $$

create procedure crearAdministrador (
in _documento varchar(40),
in _tipoDocumento int, 
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
insert into PERSONA (idPERSONA,tipoDocumento,primerNombre,segundoNombre,primerApellido,segundoApellido, direccionResidencia,email,telefono,contraseña) 
values(_documento,_tipoDocumento,_primerNombre,_segundoNombre,_primerApellido,_segundoApellido,_direccionResidencia,_email,_telefono,sha(_contraseña));
insert into ADMINISTRADOR (PERSONA_idPERSONA)values (_documento);
end $$