insert into PERSONA (idPERSONA,primerNombre,segundoNombre,primerApellido,segundoApellido, direccionResidencia,email,telefono,contraseña) 
values('12345','Antonio','','Perez','','Callefalsa123','antonio@example.com','2345678765',sha('1234'));
insert into USUARIO values ('12345');
select * from PERSONA;

call crearUsuario('12345','Antonio','','Perez','','Callefalsa123','antonio@example.com','2345678765',sha('1234'));

insert into categoria (nombre,imagen) values ('Tubérculos','/imagen/img.jpg');
insert into categoria (nombre,imagen) values ('Hortalizas','/imagen/img.jpg');

insert into PRODUCTO (CATEGORIA_idCATEGORIA,nombre,unidad,precio,imagen) 
values (1,"Papa pastusa","libra",500,"/imagen/img.jpg");

insert into permiso (nombrePermiso) values ("Crear administrador");
insert into permiso (nombrePermiso) values ("Crear domiciliario");
insert into permiso (nombrePermiso) values ("Modificar administrador");
insert into permiso (nombrePermiso) values ("Modificar domiciliario");

call crearAdministrador('12345',1,'Antonio','','Perez','','Callefalsa123','antonio@example.com','2345678765',sha('1234'))
