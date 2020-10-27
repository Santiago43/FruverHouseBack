import mysql.connector
from mysql.connector import errorcode
from dao.CategoriasDao import CategoriasDao
from dao.models import Categoria
import json
import cgi

print('Content-Type: text/json')
print('')


datos= cgi.FieldStorage()

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