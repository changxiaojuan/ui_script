from .common.page_objects import PageElement,PageObject,MultiPageElement
from selenium import webdriver

class DownloadFile(PageObject):
    #下载时弹出登录
    login_btn = PageElement(id_ = "loginbtnofpartial")
    username = PageElement(id_ = "inputUserName")
    password = PageElement(id_ = "inputPwd")
    login = PageElement(id_ = "loginByUserName")
    remember = PageElement(id_ = "remember")


    check_box = MultiPageElement(name = "recordList")#文章多选框
    down_all = PageElement(class_name  = "down-all")#批量下载按钮
    batch_download = PageElement(id_ = "batchDownload")#确定按钮

    word = PageElement(id_ = "tool-word")
    pdf = PageElement(id_ = "tool-pdf")
    txt = PageElement(id_="tool-txt")
    hyper = PageElement(id_="tool-hyper")
    pure = PageElement(id_="tool-pure")









