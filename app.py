from flask import Flask, jsonify, request
from flask_cors import CORS

from dao.UsuariosDao import UsuariosDao
from dao.PedidosDao import PedidosDao
from dao.AdminDao import AdminDao
from dao.DomiciliarioDao import DomiciliarioDao
from dao.PermisoDao import PermisoDao
from dao.models import Domiciliario, Pedido, ProductoACompra, Administrador



# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/admin', methods=['POST','GET'])
def admin():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        primerNombre=data.get('n1')
        segundoNombre=data.get('n2')
        primerApellido=data.get('a1')
        segundoApellido=data.get('a2')
        email=data.get('email')
        telefono=data.get('telefono')
        contraseña =data.get('contra')
        documento=data.get('documento')
        tipoDocumento=data.get('tipoDocumento')
        direccion=data.get('direccion')
        permisos=data.get('permisos')
        administrador=Administrador(documento,tipoDocumento,primerNombre,segundoNombre,primerApellido,segundoApellido,email,contraseña,telefono,direccion,permisos)
        dao=AdminDao()
        if(dao.consultar(email,contraseña) is None):
            if(dao.registrar(administrador)):
                response_object['mensaje']="administrador creado"
            else:
                response_object['tipo']="error"
                response_object['mensaje']="Error al crear administrador"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Ya existe un administrador con esa identificación o con ese correo"
        return jsonify(response_object)

@app.route('/domicilio', methods=['POST','GET'])
def domicilio():
    response_object = {'tipo': 'OK'}
    if request.method=="POST":
        data=request.get_json()
        primerNombre=data.get('n1')
        segundoNombre=data.get('n2')
        primerApellido=data.get('a1')
        segundoApellido=data.get('a2')
        email=data.get('email')
        telefono=data.get('telefono')
        contraseña =data.get('contra')
        documento=data.get('documento')
        tipoDocumento=data.get('tipoDocumento')
        direccion=data.get('direccion')
        idTienda = data.get('idTienda')
        domiciliario=Domiciliario(documento,tipoDocumento,primerNombre,segundoNombre,primerApellido,segundoApellido,email,contraseña,telefono,direccion,idTienda)
        dao=DomiciliarioDao()
        if(dao.consultar(email,contraseña) is None):
            if(dao.registrar(domiciliario)):
                response_object['mensaje']="domiciliario creado"
            else:
                response_object['tipo']="error"
                response_object['mensaje']="Error al crear domiciliario"
        else:
            response_object['tipo']="error"
            response_object['mensaje']="Ya existe un domiciliario con esa identificación o con ese correo"
        return jsonify(response_object)

@app.route('/compra', methods=['POST','GET'])
def compra():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data=request.get_json()
        user=data.get('user')
        items=data.get('data')
        destino=data.get('direccion')
        productosEnLista = []
        for i in items:
            productoEnPedido = ProductoACompra(i['idProducto'],i['cantidad']) 
            productosEnLista.append(productoEnPedido)
        pedido = Pedido(0,user,destino,productosEnLista)
        pedidoDao = PedidosDao()
        if pedidoDao.registrar(pedido):
            response_object['mensaje']='Compra realizada. Un domiciliario tomará el pedido'
        else:
            response_object['mensaje']='Error al realizar el pedido'
            response_object['status']='error'
        return jsonify(response_object)
    else:
        return jsonify(response_object)

@app.route('/user', methods=['GET'])
def user():
    response_object = {'status': 'success'}
    data=request.get_json()
    user=data.get('user')
    uDao = UsuariosDao()
    usuario = uDao.consultarPorId(user)
    response_object['usuario']=usuario.__dict__
    return jsonify(response_object)

@app.route('/permisos', methods=['GET'])
def permisos():
    response_object = {'status': 'success'}
    data=request.get_json()
    permDao = PermisoDao()
    permisos = permDao.consultarPermisos()
    permisojson=[]
    for permiso in permisos:
        permisojson.append(permiso.__dict__)
    response_object['permisos']=permisojson
    return jsonify(response_object)
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)