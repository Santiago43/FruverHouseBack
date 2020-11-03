update CATEGORIA
set nombre='Hortalizas', imagen='https://www.ejemplos.co/wp-content/uploads/2018/11/Hortalizas-e1543613569254.jpg'
where idCategoria=2 ; 

update PERSONA
set primerNombre='Antonio', segundoNombre='', primerApellido='Pérez', segundoApellido='Ortiz',direccionResidencia='Calle 43',email='antonio@gmail.com', telefono='320890', contraseña=sha('123')
where idPERSONA= '12345';

update PRODUCTO
set CATEGORIA_idCATEGORIA=1,nombre='Papa pastusa', imagen ='https://cdn.shopify.com/s/files/1/1382/4921/products/Papa_Pastusa_470x.jpg?v=1479351571', unidad='libra', precio=700
where idProducto = 1;
