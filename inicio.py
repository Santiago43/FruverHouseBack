#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from dao.CategoriasDao import CategoriasDao
from dao.models import Categoria
import json
import cgi
import os

print('Content-Type: text/json')
print('')


datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="GET":
    dao=CategoriasDao()
    categorias = dao.listarTodos()
    print("[")
    longitud=len(categorias)
    i=1
    for categoria in categorias:
        print(json.dumps(categoria.__dict__))
        if i<longitud:
            print(",")
            i=i+1
    print("]")