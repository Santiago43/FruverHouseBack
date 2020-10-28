import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Categoria

class CategoriasDao(dao):
    """
    Clase de objeto de acceso a datos de las categorías
    """
    
    def registrar(self,categoria):
        """ Se almacena en la base de datos una categoria
        Parámetros
        categoria --- que es la categoría que se almacenará
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "insert into categoria (nombre,imagen) values ('"+categoria.nombre+"','"+categoria.imagen+"');"
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
            else:
                print(err)
            return False
    
    def consultar(self,idCategoria):
        """ Se consultan datos de un usuario mediante correo y contraseña
        Parámetros
        email --- correo registrado del usuario
        password --- contraseña del usuario
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from CATEGORIA where idCATEGORIA="+idCategoria+";"
            cursor.execute(sql)
            categoria=None
            for row in cursor:
                categoria = Categoria(row[1],row[2])
                categoria.idCategoria=row[0]
            cursor.close()
            cnx.close()
            return categoria
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def actualizar(self,categoria):
        """Actualizar categoria
        Parámetros:
        categoria --- Categoría a actualizar
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "update CATEGORIA set nombre="+categoria.nombre+", imagen="+categoria.imagen+" where idCategoria="+categoria.idCategoria+" ; "
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
    def eliminar(self,categoria):
        """Eliminar
        Parámetros:
        categoria --- Categoría a actualizar
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "update CATEGORIA set nombre="+categoria.nombre+", imagen="+categoria.imagen+" where idCategoria="+categoria.idCategoria+" ; "
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
        categorias=[]
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from CATEGORIA;"
            cursor.execute(sql)
            for row in cursor:
                categoria=Categoria(row[1],row[2])
                categoria.idCategoria=row[0]
                categorias.append(categoria)
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
        return categorias