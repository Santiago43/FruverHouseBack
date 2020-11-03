import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Producto

class ProductosDao(dao):
    """
    Clase de objeto de acceso a datos de los productos
    """
    
    def registrar(self,producto):
        """ Se almacena en la base de datos un producto

        Parámetros
        
        producto --- que es el producto que se almacenará
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "insert into PRODUCTO (CATEGORIA_idCATEGORIA,nombre,unidad,precio,imagen)  values (%s,%s,%s,%s,%s);"
            cursor.execute(sql,(producto.idCategoria,producto.nombre,producto.unidad,producto.precio,producto.imagen))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False
    
    def consultar(self,idProducto):
        """ Se consultan datos de un producto
        Parámetros:

        idProducto --- que es el id del producto en la base de datos
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from PRODUCTO where idPRODUCTO="+str(idProducto)+";"
            cursor.execute(sql)
            producto=None
            for row in cursor:
                producto = Producto(row[1],row[2],row[3],row[4],row[5])
                producto.idProducto=row[0]
            cursor.close()
            cnx.close()
            return producto
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def actualizar(self,producto):
        """Actualizar producto

        Parámetros:
        
        producto -- producto a actualizar
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "update PRODUCTO set CATEGORIA_idCATEGORIA=%s,nombre=%s, imagen =%s, unidad=%s, precio=%s where idProducto = %s;"
            cursor.execute(sql,(producto.idCategoria,producto.nombre,producto.imagen,producto.unidad,producto.precio,producto.idProducto))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return False
    def eliminar(self,producto):
        """Eliminar

        Parámetros:
        
        categoria --- Categoría a actualizar
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "delete from PRODUCTO where idPRODUCTO="+str(producto.idProducto)+"; "
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return False
    def listarTodos(self):
        """Lista todas las categorías almacenadas en la base de datos 
        """
        productos=[]
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from PRODUCTO;"
            cursor.execute(sql)
            for row in cursor:
                producto = Producto(row[1],row[2],row[3],row[4],row[5])
                producto.idProducto=row[0]
                productos.append(producto)
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return None
        return productos
    def consultarPorCategoria(self,idCategoria):
        """Consulta productos por categoria
        """
        productos=[]
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from PRODUCTO where CATEGORIA_idCATEGORIA="+str(idCategoria)+";"
            cursor.execute(sql)
            for row in cursor:
                producto = Producto(row[1],row[2],row[3],row[4],row[5])
                producto.idProducto=row[0]
                productos.append(producto)
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return None
        return productos