import requests
import sqlite3

def test_register(username, password, expected_code, expected_msg):
    url = "http://localhost:5000/register"
    data = {"username": username, "password": password}
    
    print(f"\n测试: 用户名={username}, 密码={password}, 期望code={expected_code}")
    resp = requests.post(url, json=data)
    resp_json = resp.json()
    
    # 动态断言：状态码应该等于期望的 HTTP 状态码（200 或 409）
    assert resp.status_code == expected_code, f"HTTP状态码错误，期望{expected_code}，实际{resp.status_code}"
    # 业务 code 也应该等于期望值
    assert resp_json.get("code") == expected_code, f"业务code错误，期望{expected_code}，实际{resp_json.get('code')}"
    assert resp_json.get("message") == expected_msg, f"消息错误，期望{expected_msg}，实际{resp_json.get('message')}"
    
    print("  测试通过")
    # 如果注册成功（期望 200），返回 True，否则 False
    return expected_code == 200

# 清空数据库表，从干净状态开始
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM users")
conn.commit()
conn.close()
print("已清空 users 表，开始测试...")

# 测试1：注册新用户 alice，期望成功
test_register("alice", "123456", 200, "注册成功")

# 测试2：重复注册 alice，期望冲突 409
test_register("alice", "123456", 409, "用户名已存在")

print("\n所有测试完成。")
