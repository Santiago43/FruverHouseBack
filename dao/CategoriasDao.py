import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Categoria
"""
Clase de objeto de acceso a datos de las categorías
"""
class CategoriasDao(dao):
    """ Se almacena en la base de datos una categoria
    Parámetros
    categoria --- que es la categoría que se almacenará

    """
    def registrar(self,categoria):
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
    def consultar(self,email,password):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select p.* from PERSONA as p inner join USUARIO as u on p.idPERSONA=u.PERSONA_idPERSONA where p.email='"+email+"' and p.contraseña=sha('"+password+"');"
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

    def listarTodos(self):
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