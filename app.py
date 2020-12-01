from flask import Flask, jsonify, request
from flask_cors import CORS


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
        car_items=request.args.items()
        for (k,v) in car_items:
            print(k,v)
        print(request.view_args)
        return jsonify("ajá")
    else:
        return jsonify(response_object)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)