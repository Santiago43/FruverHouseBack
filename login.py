import mysql.connector
from mysql.connector import errorcode
from dao.UsuariosDao import UsuariosDao
from dao.models import Usuario
import cgi

print('Content-Type: text/json')
print('')


datos= cgi.FieldStorage()
email=datos.getvalue('email')
contraseña =datos.getvalue('contra')


#usuario=Usuario(cedula,primerNombre,segundoNombre,primerApellido,segundoApellido,email,contraseña,telefono,direccion)
dao=UsuariosDao()
usuario = dao.consultar(email,contraseña)
if(usuario is not None):
    print('{"tipo":"OK","mensaje","Bienvenido/a, '+usuario.primerNombre+'"}')
else:
    print('{"tipo":"error","mensaje":"Usuario o contraseña inválidos"}')