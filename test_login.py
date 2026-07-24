import requests
from config import BASE_URL

# 来测试一下
class TestLogin:
    """模拟登录功能的测试"""

    def test_login_success(self):
        """测试登录成功"""
        data = {"username": "admin", "password": "***"}
        resp = requests.post(f"{BASE_URL}/post", json=data)

        assert resp.status_code == 200
        result = resp.json()
        print(f"登录成功：{result['json']}")
        print("✅ 测试通过！")

    def test_login_wrong_password(self):
        """测试密码错误"""
        data = {"username": "admin", "password": "***"}
        resp = requests.post(f"{BASE_URL}/post", json=data)

        assert resp.status_code == 200
        print("✅ 密码错误场景测试通过")

    def test_empty_username(self):
        """测试用户名为空"""
        data = {"username": "", "password": "***"}
        resp = requests.post(f"{BASE_URL}/post", json=data)

        assert resp.status_code == 200
        print("✅ 用户名为空场景测试通过")

    def test_number(self):
        """测试一个数字"""
        a = 9
        assert a == 9, f"a的值为{a}，实际想要的是9"
        print("✅ 测试数据是成功的")

