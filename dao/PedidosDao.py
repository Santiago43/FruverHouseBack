import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Pedido
class PedidosDao(dao):
    def registrar(self,pedido):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[]
            cursor.callproc("crearAdministrador",args)
            for permiso in administrador.permisos:
                sql = "insert into ADMINISTRADOR_has_PERMISO (ADMINISTRADOR_PERSONA_idPERSONA,PERMISO_idPERMISO)  values (%s,%s);"
                cursor.execute(sql,(administrador.documento,permiso))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None