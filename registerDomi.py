#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from dao.AdminDao import AdminDao
from dao.models import Domiciliario
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
    documento=datos.getvalue('documento')
    tipoDocumento=datos.getvalue('tipoDocumento')
    direccion=datos.getvalue('direccion')
    idTienda = datos.getvalue('idTienda')

    administrador=Domiciliario(documento,tipoDocumento,primerNombre,segundoNombre,primerApellido,segundoApellido,email,contraseña,telefono,direccion,idtienda)
    dao=AdminDao()
    if(dao.consultar(email,contraseña) is None):
        if(dao.registrar(administrador)):
            print(json.dumps('{"tipo":"OK","mensaje":"administrador creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear administrador"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un administrador con esa identificación o con ese correo"}'))