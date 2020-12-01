from flask import Flask, jsonify, request
from flask_cors import CORS

from dao.models import ProductoACompra
from dao.UsuariosDao import UsuariosDao


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
    return jsonify('pong!')

@app.route('/compra', methods=['POST','GET'])
def compra():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data=request.get_json()
        user=data.get('user')
        items=data.get('data')
        productosEnLista = []
        for i in items:
            productoEnPedido = ProductoACompra(i['idProducto'],i['cantidad']) 
            productosEnLista.append(productoEnPedido)
                
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
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)