from page.page_03_search_title import SearchTitle
from time import sleep
from selenium.webdriver import ActionChains
import pytest
from selenium import webdriver


class TestSearchTitle():
    def test_search_title(self,browser,base_url):
        """
        按标题搜索
        """
        search = SearchTitle(browser)
        search.get(base_url)
        sleep(2)
        ele = search.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(2)
        search.select_title.click()
        sleep(2)
        search.search_box.send_keys("全国人民代表大会")
        search.search_btn.click()

    def test_search_title_dim(self, browser, base_url):
        """
        按标题模糊搜索
        """
        search = SearchTitle(browser)
        search.get(base_url)
        sleep(2)
        ele = search.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(2)
        search.select_title.click()
        sleep(2)
        search.search_box.send_keys("全国人民代表大会")
        search.fuzzy.click()
        search.search_btn.click()

    def test_search_title_accurate(self, browser, base_url):
        """
        按标题精确搜索
        """
        search = SearchTitle(browser)
        search.get(base_url)
        sleep(2)
        ele = search.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(2)
        search.select_title.click()
        sleep(2)
        search.search_box.send_keys("全国人民代表大会")
        search.accurate.click()
        search.search_btn.click()

    def test_search_title_result_search(self, browser, base_url):
        """
        按标题搜索后，清空搜索内容，再在结果中搜索
        """
        search = SearchTitle(browser)
        search.get(base_url)
        sleep(2)
        ele = search.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(2)
        search.select_title.click()
        sleep(2)
        search.search_box.send_keys("全国人民代表大会")
        search.accurate.click()
        search.search_btn.click()
        search.delete_btn.click()
        search.search_box.send_keys("通知")
        search.search_btn.click()
        sleep(3)
    def test_search_title_result_search(self, browser, base_url):
        """
        按标题搜索后，清空搜索内容，再在结果中搜索
        """
        search = SearchTitle(browser)
        search.get(base_url)
        sleep(2)
        ele = search.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(2)
        search.select_title.click()
        sleep(2)
        search.search_box.send_keys("全国人民代表大会")
        search.accurate.click()
        search.search_btn.click()
        search.delete_btn.click()
        search.search_box.send_keys("通知")
        search.search_btn.click()
        sleep(3)





if __name__ == '__main__':
    pytest.main(["-v","-s","./test_03_search_title.py"])


