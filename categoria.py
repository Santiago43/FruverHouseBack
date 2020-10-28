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
if os.environ['REQUEST_METHOD']=="POST":
    dao=CategoriasDao()
    categoria = Categoria(datos.getvalue('nombre'),datos.getvalue('imagen'))
    if dao.registrar(categoria):
        print('{"tipo":"OK",mensaje:"Categoría creada"}')
    else:
        print('{"tipo":"error", "mensaje":"error al crear la categoria"}')

elif os.environ['REQUEST_METHOD']=="PUT":
    dao=CategoriasDao()
    categoria = dao.consultar(datos.getvalue('id'))
    if categoria is None:
        print('{"tipo":"error", "mensaje":"Esa categoría no existe"}')
    else:
        if datos.getvalue('nombre') is not None:
            categoria.nombre = datos.getvalue('nombre')
        if datos.getvalue('imagen') is not None:
            categoria.imagen = datos.getvalue('imagen')
        if dao.actualizar(categoria):
            print('{"tipo":"OK", "mensaje":"Categoría creada"}')
        else:
            print('{"tipo":"error", "mensaje":"error al actualizar la categoria"}')
elif os.environ['REQUEST_METHOD']=="DELETE":
    dao=CategoriasDao()
    categoria = dao.consultar(datos.getvalue('id'))
    if categoria is None:
        print(json.dumps('{"tipo":"error", "mensaje":"Esa categoría no existe"}'))
    else:
        if dao.eliminar(categoria):
            print('{"tipo":"OK", "mensaje":"Categoría eliminada"}')
        else:
            print('{"tipo":"error", "mensaje":"error al eliminar la categoria"}')

elif os.environ['REQUEST_METHOD']=="GET":
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