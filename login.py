#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from dao.UsuariosDao import UsuariosDao
from dao.AdminDao import AdminDao
from dao.DomiciliarioDao import DomiciliarioDao
from dao.models import Usuario
import json
import cgi
import os
"""
Archivo de login: permite al usuario dar paso a la página como usuario autenticado
"""
print('Content-Type: text/json')
print('')
datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="POST":
    email=datos.getvalue('email')
    contraseña =datos.getvalue('contra')
    usuariosdao=UsuariosDao()
    admindao = AdminDao()
    domiciliarioDao= DomiciliarioDao()
    usuario = usuariosdao.consultar(email,contraseña)
    admin = admindao.consultar(email,contraseña)
    domiciliario=domiciliarioDao.consultar(email,contraseña)
    if(usuario is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+usuario.primerNombre+'","usuario":'+json.dumps(usuario.__dict__)+'}'))
    elif(domiciliario is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+domiciliario.primerNombre+'","usuario":'+json.dumps(domiciliario.__dict__)+'}'))
    elif (admin is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+admin.primerNombre+'","usuario":'+json.dumps(admin.__dict__)+'}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Usuario o contraseña inválidos"}'))