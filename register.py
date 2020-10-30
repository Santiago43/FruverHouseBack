#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from dao.UsuariosDao import UsuariosDao
from dao.models import Usuario
import json
import cgi
import os

print('Content-Type: text/json')
print('')

if os.environ['REQUEST_METHOD']=="POST":
    datos= cgi.FieldStorage()
    primerNombre=datos.getvalue('n1')
    segundoNombre=datos.getvalue('n2')
    primerApellido=datos.getvalue('a1')
    segundoApellido=datos.getvalue('a2')
    email=datos.getvalue('email')
    telefono=datos.getvalue('telefono')
    contraseña =datos.getvalue('contra')
    documento=datos.getvalue('cedula')
    tipoDocumento=datos.getvalue('tipoDocumento')
    direccion=datos.getvalue('direccion')

    usuario=Usuario(documento,tipoDocumento,primerNombre,segundoNombre,primerApellido,segundoApellido,email,contraseña,telefono,direccion)
    dao=UsuariosDao()
    if(dao.consultar(email,contraseña) is None):
        if(dao.registrar(usuario)):
            print(json.dumps('{"tipo":"OK","mensaje":"Usuario creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear usuario"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un usuario con esa identificación o con ese correo"}'))
