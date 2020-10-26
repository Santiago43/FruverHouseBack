insert into PERSONA (idPERSONA,primerNombre,segundoNombre,primerApellido,segundoApellido, direccionResidencia,email,telefono,contraseña) 
values('12345','Antonio','','Perez','','Callefalsa123','antonio@example.com','2345678765',sha('1234'));
insert into USUARIO values ('12345');
select * from PERSONA;

call crearUsuario('12345','Antonio','','Perez','','Callefalsa123','antonio@example.com','2345678765',sha('1234'))