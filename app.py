from flask import Flask, jsonify, request
from flask_cors import CORS

from dao.models import ProductoACompra


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
        items=data.get('data')
        for i in items:
            print(i)
        return jsonify(response_object)
    else:
        return jsonify(response_object)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)