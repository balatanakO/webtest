import requests
from datetime import datetime

def send_request(url, data):
    """发送POST请求，返回响应对象"""
    try:
        resp = requests.post(url, json=data, timeout=5)
        return resp
    except Exception as e:
        print(f"请求失败: {e}")
        return None

# 测试数据集
test_cases = [
    {"username": "alice", "password": "123", "expected_status": 200, "expected_code": 200, "expected_msg": "注册成功"},
    {"username": "alice", "password": "123", "expected_status": 409, "expected_code": 409, "expected_msg": "用户名已存在"},
    {"username": "bob",   "password": "",     "expected_status": 400, "expected_code": 400, "expected_msg": "密码不能为空"},
]

# 打开结果文件（追加模式）
with open("result.txt", "a", encoding="utf-8") as f:
    f.write(f"\n--- 测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

    for i, case in enumerate(test_cases, 1):
        print(f"\n执行用例 {i}: username={case['username']}")
        resp = send_request("http://localhost:5000/register",
                            {"username": case["username"], "password": case["password"]})

        if resp is None:
            print("  请求失败，跳过断言")
            result = "失败"
            status_code = "N/A"
        else:
            status_code = resp.status_code
            # 检查状态码
            if status_code == case["expected_status"]:
                print(f"  ✅ 状态码正确: {status_code}")
                # 尝试解析JSON并检查业务码和消息
                try:
                    body = resp.json()
                    if body.get("code") == case["expected_code"] and body.get("message") == case["expected_msg"]:
                        print(f"  ✅ 业务code和消息正确")
                        result = "通过"
                    else:
                        print(f"  ❌ 业务code或消息错误: 期望({case['expected_code']},{case['expected_msg']}) 实际({body.get('code')},{body.get('message')})")
                        result = "失败"
                except:
                    print("  ⚠️ 响应体不是JSON")
                    result = "失败"
            else:
                print(f"  ❌ 状态码错误: 期望 {case['expected_status']}, 实际 {status_code}")
                result = "失败"

        # 写入结果到文件
        line = f"{datetime.now().strftime('%H:%M:%S')},{case['username']},{status_code},{result}\n"
        f.write(line)
        print(f"已写入结果: {line.strip()}")

print("\n测试执行完毕，结果已保存到 result.txt")
# 测试修改
