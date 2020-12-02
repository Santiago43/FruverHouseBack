#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from dao.DomiciliarioDao import DomiciliarioDao
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

    domiciliario=Domiciliario(documento,tipoDocumento,primerNombre,segundoNombre,primerApellido,segundoApellido,email,contraseña,telefono,direccion,idTienda)
    dao=DomiciliarioDao()
    if(dao.consultar(email,contraseña) is None):
        if(dao.registrar(domiciliario)):
            print(json.dumps('{"tipo":"OK","mensaje":"domiciliario creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear domiciliario"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un domiciliario con esa identificación o con ese correo"}'))