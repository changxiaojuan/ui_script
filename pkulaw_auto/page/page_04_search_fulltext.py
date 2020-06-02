from .common.page_objects import PageElement,PageObject,MultiPageElement
from selenium import webdriver

class SearchFullText(PageObject):
    select = PageElement(class_name = "areajSelect")#选择标题还是正文元素
    select_fulltext = PageElement(xpath = "/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/ul/li[3]/a")  # 选择全文
    select_title = PageElement(xpath="/html/body/div[4]/div/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a")  # 选择标题
    search_box = PageElement(id_ = "txtSearch")#搜索框
    search_btn = PageElement(id_ = "btnSearch")#搜索按钮

    fuzzy = PageElement(id_ = "like")#模糊
    accurate = PageElement(id_ = "accurate")#精确
    result_search = PageElement(link_text = "结果中检索")#结果中检索
    delete_btn = PageElement(xpath = "/html/body/div[4]/div/div[1]/div[1]/div[2]/div[2]/div/a")#输入框删除按钮


    piece = PageElement(id_ = "Piece")#同篇
    strip = PageElement(id_ = "Strip")#同条
    seg = PageElement(id_ = "Seg")#同段
    sen = PageElement(id_ = "Sen")#周条

    check_result = PageElement(class_name = "hitClass")
    #check_result = MultiPageElement(class_name = "hitClass")







