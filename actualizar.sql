update CATEGORIA
set nombre='Tubérculo', imagen='/img/img.jpg'
where idCategoria=1 ; 

update PERSONA
set primerNombre='Antonio', segundoNombre='', primerApellido='Pérez', segundoApellido='Ortiz',direccionResidencia='Calle 43',email='antonio@gmail.com', telefono='320890', contraseña=sha('123')
where idPERSONA= '12345';

update PRODUCTO
set CATEGORIA_idCATEGORIA=1,nombre='Papa pastusa', imagen ='/img/img.jpg', unidad='libra', precio=700
where idProducto = 1;