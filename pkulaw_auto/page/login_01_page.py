from .common.page_objects import PageElement,PageObject,MultiPageElement
from selenium import webdriver

class Login(PageObject):

    register = PageElement(id_ = "newloginbtn")
    username = PageElement(id_ = "inputUserName")
    password = PageElement(id_ = "inputPwd")
    login_btu = PageElement(id_ = "loginByUserName")
    remember = PageElement(id_ = "remember")
    logout = PageElement(link_text = "退出")
    login_msg = PageElement(id_ = "pwdTips")
    login_user_msg = PageElement(id_ = "userTips")
    login_pwd_msg = PageElement(id_ = "pwdTips")





