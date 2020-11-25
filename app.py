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
        post_data = request.get_json()
        response_object['message'] = 'Book added!'
    else:
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()