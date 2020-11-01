import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Usuario
class UsuariosDao(dao):
    """
    Clase de objeto de acceso a datos de los usuarios
    """
    def registrar(self,usuario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[usuario.documento,usuario.tipoDocumento,usuario.primerNombre,usuario.segundoNombre,usuario.primerApellido,usuario.segundoApellido,usuario.direccion,usuario.email,usuario.telefono,usuario.contraseña]
            cursor.callproc("crearUsuario",args)
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

    def consultar(self,email,password):
        """
        Método encargado de consultar los datos de un usuario a partir de su correo y su contraseña.

        Parámetros:

        email -- que es el correo del usuario
        
        password -- que es la contraseña del usuario
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select p.* from PERSONA as p inner join USUARIO as u on p.idPERSONA=u.PERSONA_idPERSONA where p.email='"+email+"' and p.contraseña=sha('"+password+"');"
            cursor.execute(sql)
            usuario=None
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
                usuario=Usuario(documento,tipoDocumento,primerNombre,primerApellido,segundoNombre,segundoApellido,direccion,email,contraseña,telefono)
            cursor.close()
            cnx.close()
            return usuario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def actualizar(self,usuario):
        """
        Método que actualiza los datos de un usuario
        Parámetros:
        usuario - que es el usuario que se va a actualizar en la base de datos
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "update PERSONA set tipoDocumento='"+usuario.tipoDocumento+"'primerNombre='"+usuario.primerNombre+"', segundoNombre='"+usuario.segundoNombre+"', primerApellido='"+usuario.primerApellido+"', segundoApellido='"+usuario.segundoApellido+"',direccionResidencia='"+usuario.direccion+"',email='"+usuario.email+"', telefono='"+usuario.telefono+"', contraseña=sha('"+usuario.contraseña+"') where idPERSONA= '"+usuario.cedula+"';"
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
    