import requests

url = "http://localhost:5000/register"
data = {"username": "testuser1", "password": "123456"}

resp = requests.post(url, json=data)

print("状态码:", resp.status_code)
print("返回内容:", resp.text)

assert resp.status_code == 200
assert resp.json()["code"] == 200
assert resp.json()["message"] == "注册成功"

print("测试通过")
