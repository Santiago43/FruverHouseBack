update CATEGORIA
set nombre='Tubérculo', imagen='https://totalsaludable.com/wp-content/uploads/2020/06/Tub%C3%A9rculos-1-750x450.jpg'
where idCategoria=1 ; 

update PERSONA
set primerNombre='Antonio', segundoNombre='', primerApellido='Pérez', segundoApellido='Ortiz',direccionResidencia='Calle 43',email='antonio@gmail.com', telefono='320890', contraseña=sha('123')
where idPERSONA= '12345';

update PRODUCTO
set CATEGORIA_idCATEGORIA=1,nombre='Papa pastusa', imagen ='https://cdn.shopify.com/s/files/1/1382/4921/products/Papa_Pastusa_470x.jpg?v=1479351571', unidad='libra', precio=700
where idProducto = 1;