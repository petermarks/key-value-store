from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
store = {}

@app.route('/item/<path:key>', methods=['GET'])
def get_value(key):
    if key in store:
        return store[key]
    else:
        return f'Key "{key}" not found', 404

@app.route('/item/<path:key>', methods=['PUT'])
def put_value(key):
    value = request.data.decode('utf-8')
    store[key] = value
    return f'Successfully stored value "{value}" with key "{key}"'

@app.route('/dump', methods=['GET'])
def dump_store():
    return jsonify(store)

@app.route('/dashboard')
def dashboard():
    return send_file('static/dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
