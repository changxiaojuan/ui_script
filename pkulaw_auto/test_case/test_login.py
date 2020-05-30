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

    def test_login_usererror(self, browser, base_url, username, password):
        """
        测试登录，用户名错误
        """
        login = Login(browser)
        login.get(base_url)
        sleep(1)
        login.register.click()
        sleep(2)
        login.username.send_keys("dbt")
        login.password.send_keys(password)
        login.login_btu.click()
        sleep(1)
        print(login.login_msg.text)
        assert "用户名或密码错误。" == login.login_msg.text

    def test_login_pwderror(self, browser, base_url, username, password):
        """
        测试登录，密码错误
        """
        login = Login(browser)
        login.get(base_url)
        sleep(1)
        login.register.click()
        sleep(2)
        login.username.send_keys(username)
        login.password.send_keys(111)
        login.login_btu.click()
        sleep(1)
        print(login.login_msg.text)
        assert "用户名或密码错误。" == login.login_msg.text

    def test_login_usernull(self, browser, base_url, username, password):
        """
        测试登录，用户名为空
        """
        login = Login(browser)
        login.get(base_url)
        sleep(1)
        login.register.click()
        sleep(2)
        login.username.send_keys("")
        login.password.send_keys(password)
        login.login_btu.click()
        sleep(1)
        print(login.login_user_msg.text)
        assert "请输入用户名！" == login.login_user_msg.text

    def test_login_pwdnull(self, browser, base_url, username, password):
        """
        测试登录，密码为空
        """
        login = Login(browser)
        login.get(base_url)
        sleep(1)
        login.register.click()
        sleep(2)
        login.username.send_keys(username)
        login.password.send_keys("")
        login.login_btu.click()
        sleep(1)
        print(login.login_pwd_msg.text)
        assert "请输入密码！" == login.login_pwd_msg.text




        sleep(5)




if __name__ == '__main__':
    pytest.main(["-v","-s","./test_login.py"])