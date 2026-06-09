from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/user')
def get_user():
    return jsonify({"code": 200, "data": {"name": "张三", "age": 25}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
