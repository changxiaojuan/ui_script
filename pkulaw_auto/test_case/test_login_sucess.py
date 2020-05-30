from page.login_page import Login
from time import sleep
import pytest

class TestLogin:
    def test_login_sucsess(self,browser,base_url,username,password):
        """
        测试登录成功
        """
        login = Login(browser)
        login.get(base_url)
        sleep(1)
        login.register.click()
        sleep(2)
        login.username.send_keys(username)
        login.password.send_keys(password)
        login.login_btu.click()
        sleep(1)
        assert "退出" == login.logout.text
        sleep(5)
        login.logout.click()