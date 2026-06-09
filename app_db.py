from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 初始化数据库：创建 users 表
def init_db():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"code": 400, "message": "用户名和密码不能为空"}), 400

    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return jsonify({"code": 200, "message": "注册成功"}), 200
    except sqlite3.IntegrityError:
        return jsonify({"code": 409, "message": "用户名已存在"}), 409

if __name__ == '__main__':
    init_db()   # 启动时初始化表
    app.run(host='0.0.0.0', port=5000)
