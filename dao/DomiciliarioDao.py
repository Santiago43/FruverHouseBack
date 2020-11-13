import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Domiciliario
class DomiciliarioDao(dao):
    """
    Clase de objeto de acceso a datos de los domiciliarios
    """
    def registrar(self,domiciliario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[domiciliario.documento,domiciliario.tipoDocumento,domiciliario.primerNombre,domiciliario.segundoNombre,domiciliario.primerApellido,domiciliario.segundoApellido,domiciliario.direccion,domiciliario.email,domiciliario.telefono,domiciliario.contraseña]
            cursor.callproc("creardomiciliario",args)
            for permiso in domiciliario.permisos:
                sql = "insert into DOMICILARIO_has_PERMISO (domiciliario_PERSONA_idPERSONA,PERMISO_idPERMISO)  values (%s,%s);"
                cursor.execute(sql,(domiciliario.documento,permiso))
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

    def consultar(self,email,password):
        """
        Método encargado de consultar los datos de un domiciliario a partir de su correo y su contraseña.

        Parámetros:

        email -- que es el correo del domiciliario
        
        password -- que es la contraseña del domiciliario
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select p.* from PERSONA as p inner join DOMICILIARIO as d on p.idPERSONA=d.PERSONA_idPERSONA where p.email='"+email+"' and p.contraseña=sha('"+password+"');"
            cursor.execute(sql)
            domiciliario=None
            for row in cursor:
                documento=row[0]
                tipoDocumento=row[1]
                primerNombre=row[2]
                segundoNombre=row[3]
                primerApellido=row[4]
                segundoApellido=row[5]
                direccion=row[6]
                email=row[7]
                contraseña=row[8]
                telefono=row[9]
                domiciliario=Domiciliario(documento,tipoDocumento,primerNombre,primerApellido,segundoNombre,segundoApellido,direccion,email,contraseña,telefono,None)
            cursor.close()
            cnx.close()
            return domiciliario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def actualizar(self,domiciliario):
        """
        Método que actualiza los datos de un domiciliario
        Parámetros:
        domiciliario - que es el domiciliario que se va a actualizar en la base de datos
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "update PERSONA set tipoDocumento='"+domiciliario.tipoDocumento+"'primerNombre='"+domiciliario.primerNombre+"', segundoNombre='"+domiciliario.segundoNombre+"', primerApellido='"+domiciliario.primerApellido+"', segundoApellido='"+domiciliario.segundoApellido+"',direccionResidencia='"+domiciliario.direccion+"',email='"+domiciliario.email+"', telefono='"+domiciliario.telefono+"', contraseña=sha('"+domiciliario.contraseña+"') where idPERSONA= '"+domiciliario.documento+"';"
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
    