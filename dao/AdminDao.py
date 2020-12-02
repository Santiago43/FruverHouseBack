import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Administrador
class AdminDao(dao):
    """
    Clase de objeto de acceso a datos de los administradors
    """
    def registrar(self,administrador):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[administrador.documento,administrador.tipoDocumento,administrador.primerNombre,administrador.segundoNombre,administrador.primerApellido,administrador.segundoApellido,administrador.direccion,administrador.email,administrador.telefono,administrador.contraseña]
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

    def consultar(self,email,password):
        """
        Método encargado de consultar los datos de un administrador a partir de su correo y su contraseña.

        Parámetros:

        email -- que es el correo del administrador
        
        password -- que es la contraseña del administrador
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select p.* from PERSONA as p inner join ADMINISTRADOR as a on p.idPERSONA=a.PERSONA_idPERSONA where p.email='"+email+"' and p.contraseña=sha('"+password+"');"
            cursor.execute(sql)
            administrador=None
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
                administrador=Administrador(documento,tipoDocumento,primerNombre,primerApellido,segundoNombre,segundoApellido,direccion,email,contraseña,telefono,None)
            sql2= "select p.nombrePermiso from PERMISO as p inner join ADMINISTRADOR_has_PERMISO as ap on p.idPERMISO=ap.PERMISO_idPERMISO inner join ADMINISTRADOR as a on ap.ADMINISTRADOR_PERSONA_idPERSONA=a.PERSONA_idPERSONA where a.PERSONA_idPERSONA='"+administrador.documento+"'"
            cursor.execute(sql2)
            permisos = []
            for row in cursor:
                permisos.append(row[0])
            administrador.permisos=permisos
            cursor.close()
            cnx.close()
            return administrador
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def actualizar(self,administrador):
        """
        Método que actualiza los datos de un administrador
        Parámetros:
        administrador - que es el administrador que se va a actualizar en la base de datos
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "update PERSONA set tipoDocumento='"+administrador.tipoDocumento+"'primerNombre='"+administrador.primerNombre+"', segundoNombre='"+administrador.segundoNombre+"', primerApellido='"+administrador.primerApellido+"', segundoApellido='"+administrador.segundoApellido+"',direccionResidencia='"+administrador.direccion+"',email='"+administrador.email+"', telefono='"+administrador.telefono+"', contraseña=sha('"+administrador.contraseña+"') where idPERSONA= '"+administrador.documento+"';"
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

    def consultarPorId(self,documento):
        """
        Método encargado de consultar los datos de un administrador a partir de su número de documento.

        Parámetros:

        documento -- que es el número de documento del administrador
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select p.* from PERSONA as p inner join administrador as a on p.idPERSONA=a.PERSONA_idPERSONA where p.idPERSONA='"+documento+"';"
            cursor.execute(sql)
            administrador=None
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
                administrador=Administrador(documento,tipoDocumento,primerNombre,primerApellido,segundoNombre,segundoApellido,direccion,email,contraseña,telefono,None)
            sql2= "select p.nombrePermiso from PERMISO as p inner join ADMINISTRADOR_has_PERMISO as ap on p.idPERMISO=ap.PERMISO_idPERMISO inner join ADMINISTRADOR as a on ap.ADMINISTRADOR_PERSONA_idPERSONA=a.PERSONA_idPERSONA where a.PERSONA_idPERSONA='"+administrador.documento+"'"
            cursor.execute(sql2)
            permisos = []
            for row in cursor:
                permisos.append(row[0])
            administrador.permisos=permisos
            cursor.close()
            cnx.close()
            return administrador
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None