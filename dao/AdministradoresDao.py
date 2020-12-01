import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Administrador
class AdministradoresDao(dao):
    """
    Clase de objeto de acceso a datos de los usuarios
    """
    def registrarAdmin(self,administrador):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[administrador.documento,administrador.tipoDocumento,administrador.primerNombre,administrador.segundoNombre,administrador.primerApellido,administrador.segundoApellido,administrador.direccion,administrador.email,administrador.telefono,administrador.contraseña,administrador.permisos]
            cursor.callproc("crearAdministrador",args)
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

    def consultarAdmin(self,email,password):
        """
        Método encargado de consultar los datos de un usuario a partir de su correo y su contraseña.

        Parámetros:

        email -- que es el correo del usuario
        
        password -- que es la contraseña del usuario
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select p.* from PERSONA as p inner join ADMINISTRADOR as u on p.idPERSONA=u.PERSONA_idPERSONA where p.email='"+email+"' and p.contraseña=sha('"+password+"');"
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
                permisos=row[10]
                administrador=Administrador(documento,tipoDocumento,primerNombre,primerApellido,segundoNombre,segundoApellido,direccion,email,contraseña,telefono,permisos)
            cursor.close()
            cnx.close()
            return administrador
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def actualizarAdmin(self,administrador):
        """
        Método que actualiza los datos de un usuario
        Parámetros:
        usuario - que es el usuario que se va a actualizar en la base de datos
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "update PERSONA set tipoDocumento='"+administrador.tipoDocumento+"'primerNombre='"+administrador.primerNombre+"', segundoNombre='"+administrador.segundoNombre+"', primerApellido='"+administrador.primerApellido+"', segundoApellido='"+administrador.segundoApellido+"',direccionResidencia='"+administrador.direccion+"',email='"+administrador.email+"', telefono='"+administrador.telefono+"', contraseña=sha('"+administrador.contraseña+"', permisos='"+administrador.permisos+"') where idPERSONA= '"+administrador.cedula+"';"
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
    