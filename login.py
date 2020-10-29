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
datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="POST":
    email=datos.getvalue('email')
    contraseña =datos.getvalue('contra')
    dao=UsuariosDao()
    usuario = dao.consultar(email,contraseña)
    if(usuario is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+usuario.primerNombre+'"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Usuario o contrasena inválidos"}'))