import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Permiso
class PermisoDao(dao):
    def consultarPermisos(self):
        """ Se consultan los permisos existentes
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from PERMISO;"
            cursor.execute(sql)
            permisos=[]
            permiso=None
            for row in cursor:
                permiso = Permiso(row[1])
                permiso.idPermiso=row[0]
                permisos.append(permiso)
            cursor.close()
            cnx.close()
            return permisos
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None