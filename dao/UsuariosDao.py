import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Usuario
"""
import sys
sys.path
sys.path.append('/FruverHouseBack/modelo/usuarios.py')
"""
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
            sql = "insert into USUARIO (PERSONA_idPERSONA) values (%s)"
            cursor.execute(sql,usuario.cedula)
            cursor.commit()
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
                cedula=row[0]
                primerNombre=row[1]
                segundoNombre=row[2]
                primerApellido=row[3]
                segundoApellido=row[4]
                direccion=row[5]
                email=row[6]
                contraseña=row[7]
                telefono=row[8]
                usuario=Usuario(cedula,primerNombre,primerApellido,segundoNombre,segundoApellido,direccion,email,contraseña,telefono)
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