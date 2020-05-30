from .common.page_objects import PageElement,PageObject,MultiPageElement
from selenium import webdriver

class SearchTitle(PageObject):
    select = PageElement(class_name = "areajSelect")#选择标题还是正文元素
    select_title = PageElement(xpath = "/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a")#选择标题
    select_title = PageElement(xpath = "/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a")
    search_box = PageElement(id_ = "txtSearch")#搜索框
    search_btn = PageElement(id_ = "btnSearch")#搜索按钮

    fuzzy = PageElement(id_ = "like")#模糊
    accurate = PageElement(id_ = "accurate")#精确
    result_search = PageElement(link_text = "结果中检索")#结果中检索
    delete_btn = PageElement(xpath = "/html/body/div[4]/div/div[1]/div[1]/div[2]/div[2]/div/a")#输入框删除按钮



