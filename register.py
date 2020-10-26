#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from dao.UsuariosDao import UsuariosDao
from modelo.usuarios import Usuario
import cgi

print('Content-Type: text/json')
print('')


datos= cgi.FieldStorage()
primerNombre=datos.getvalue('n1')
segundoNombre=datos.getvalue('n2')
primerApellido=datos.getvalue('a1')
segundoApellido=datos.getvalue('a2')
email=datos.getvalue('email')
telefono=datos.getvalue('telefono')
contraseña =datos.getvalue('contra')
cedula=datos.getvalue('cedula')
direccion=datos.getvalue('direccion')

usuario=Usuario(cedula,primerNombre,segundoNombre,primerApellido,segundoApellido,email,contraseña,telefono,direccion)
dao=UsuariosDao()
if(dao.consultar(usuario.email,usuario.password) is None):
    if(dao.registrar(usuario)):
        print('{"mensaje":"Usuario creado"}')
    else:
        print('{"mensaje":"Ese usuario ya existe"}')
