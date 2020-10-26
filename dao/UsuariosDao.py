import mysql.connector
from mysql.connector import errorcode
from dao import dao
from FruverHouseBack.modelo.usuarios import Usuario
class UsuariosDao(dao):
    """
    docstring
    """
    def registrar(self,usuario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "insert into PERSONA (idPERSONA,primerNombre,segundoNombre,primerApellido,segundoApellido, direccionResidencia,email,contraseña,telefono) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql,(usuario.cedula,usuario.primerNombre,usuario.segundoNombre,usuario.primerApellido,usuario.segundoApellido,usuario.direccion,usuario.email,usuario.contraseña,usuario.telefono))
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
            sql = "select * from PERSONA where email='"+email+"'and contraseña=sha('"+password+"');"
            cursor.execute(sql)
            for row in cursor:
                usuario = Usuario()
                usuario.cedula=row[0]
                usuario.primerNombre=row[1]
                usuario.segundoNombre=row[2]
                usuario.primerApellido=row[3]
                usuario.segundoApellido=row[4]
                usuario.direccion=row[5]
                usuario.email=row[6]
                usuario.contraseña=row[7]
                usuario.telefono=row[8]
            cursor.close()
            cnx.close()
            return usuario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return None