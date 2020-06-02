from page.page_04_search_fulltext import SearchFullText
from time import sleep
import pytest
from selenium.webdriver import ActionChains

class TestSearchFullText():
    def test_search_fulltext_accurate(self,browser,base_url):
        """
        全文精确检索
        """
        search_fulltext = SearchFullText(browser)
        search_fulltext.get(base_url)
        sleep(2)
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_fulltext.click()
        search_fulltext.search_box.send_keys("全国人民代表大会")
        search_fulltext.search_btn.click()
        sleep(1)
        assert "全国人民代表大会" == search_fulltext.check_result.text

    def test_search_fulltext_fuzzy(self, browser, base_url):
        """
         全文模糊检索
        """
        search_fulltext = SearchFullText(browser)
        search_fulltext.get(base_url)
        sleep(2)
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_fulltext.click()
        search_fulltext.search_box.send_keys("全国人民代表大会")
        search_fulltext.fuzzy.click()
        search_fulltext.search_btn.click()
        sleep(1)
        assert "全国人民代表大会" == search_fulltext.check_result.text

    def test_search_fulltext_titleswitchfuzzy(self, browser, base_url):
        """
        标题检索后，切换为全文检索
        """
        search_fulltext = SearchFullText(browser)
        search_fulltext.get(base_url)
        sleep(2)
        #先按标题检索
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_title.click()
        search_fulltext.search_box.send_keys("全国人民代表大会")
        search_fulltext.search_btn.click()
        sleep(1)
        assert "全国人民代表大会" == search_fulltext.check_result.text
        #切换全文，换关键字检索
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_fulltext.click()
        search_fulltext.delete_btn.click()
        search_fulltext.search_box.send_keys("会议")
        search_fulltext.search_btn.click()
        sleep(1)
        assert "会议" == search_fulltext.check_result.text

    def test_search_fulltext_fuzzy_piece(self, browser, base_url):
        """
        全文精确按同篇检索
        """
        search_fulltext = SearchFullText(browser)
        search_fulltext.get(base_url)
        sleep(2)
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_fulltext.click()
        search_fulltext.search_box.send_keys("通知")
        search_fulltext.piece.click()
        search_fulltext.search_btn.click()
        sleep(1)
        assert "通知" == search_fulltext.check_result.text

    def test_search_fulltext_fuzzy_strip(self, browser, base_url):
        """
        全文精确按同条检索
        """
        search_fulltext = SearchFullText(browser)
        search_fulltext.get(base_url)
        sleep(2)
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_fulltext.click()
        search_fulltext.search_box.send_keys("法律")
        search_fulltext.strip.click()
        search_fulltext.search_btn.click()
        sleep(1)
        assert "法律" == search_fulltext.check_result.text

    def test_search_fulltext_fuzzy_seg(self, browser, base_url):
        """
        全文精确按同段检索
        """
        search_fulltext = SearchFullText(browser)
        search_fulltext.get(base_url)
        sleep(2)
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_fulltext.click()
        search_fulltext.search_box.send_keys("法律")
        search_fulltext.seg.click()
        search_fulltext.search_btn.click()
        sleep(1)
        assert "法律" == search_fulltext.check_result.text

    def test_search_fulltext_fuzzy_sen(self, browser, base_url):
        """
        全文精确按同句检索
        """
        search_fulltext = SearchFullText(browser)
        search_fulltext.get(base_url)
        sleep(2)
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_fulltext.click()
        search_fulltext.search_box.send_keys("司法")
        search_fulltext.sen.click()
        search_fulltext.search_btn.click()
        sleep(1)
        assert "司法" == search_fulltext.check_result.text

    def test_search_fulltext_fuzzy_resultserarch(self, browser, base_url):
        """
        全文精确检索后，再按结果中检索
        """
        search_fulltext = SearchFullText(browser)
        search_fulltext.get(base_url)
        sleep(2)
        ele = search_fulltext.select
        ActionChains(browser).move_to_element(ele).perform()
        sleep(1)
        search_fulltext.select_fulltext.click()
        search_fulltext.search_box.send_keys("司法")
        search_fulltext.sen.click()
        search_fulltext.search_btn.click()
        sleep(1)
        assert "司法" == search_fulltext.check_result.text
        #结果中查找
        search_fulltext.delete_btn.click()
        search_fulltext.search_box.send_keys("案例")
        search_fulltext.search_btn.click()
        sleep(1)
        assert "司法" or "案例" == search_fulltext.check_result.text




        sleep(2)







if __name__ == '__main__':
    pytest.main(["-v","-s","./test_04_search_fulltext.py"])