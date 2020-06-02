from page.page_05_download_file import DownloadFile
from time import sleep
import pytest

class Testdownload_file():
    def test_download_file_excel(self,browser,base_url,username,password):
        """
        未登录时点击批量下载
        """
        download = DownloadFile(browser)
        download.get(base_url)
        ele = download.check_box
        for i in range(4):
            ele[i].click()
        download.down_all.click()
        sleep(2)
        if download.login_btn :
            #如果未登录则先登录
            sleep(1)
            download.login_btn.click()
            sleep(2)
            download.username.send_keys(username)
            download.password.send_keys(password)
            download.remember.click()
            download.login.click()
            sleep(2)
            ele = download.check_box
            for i in range(4):
                ele[i].click()
            download.down_all.click()
            sleep(1)
        download.batch_download.click()


    def test_download_file_word(self, browser, base_url):
        """
        批量下载word
        """
        download = DownloadFile(browser)
        download.get(base_url)
        ele = download.check_box
        for i in range(4):
            ele[i].click()
        download.down_all.click()
        sleep(2)
        download.word.click()
        sleep(1)
        download.batch_download.click()

    def test_download_file_pdf(self, browser, base_url):
        """
        批量下载pdf
        """
        download = DownloadFile(browser)
        download.get(base_url)
        ele = download.check_box
        for i in range(4):
            ele[i].click()
        download.down_all.click()
        sleep(1)
        download.pdf.click()
        sleep(1)
        download.batch_download.click()

    def test_download_file_txt(self, browser, base_url):
        """
        批量下载纯文本
        """
        download = DownloadFile(browser)
        download.get(base_url)
        ele = download.check_box
        for i in range(4):
            ele[i].click()
        download.down_all.click()
        sleep(1)
        download.txt.click()
        sleep(1)
        download.batch_download.click()

    def test_download_file_hyper(self, browser, base_url):
        """
        批量下载超文本
        """
        download = DownloadFile(browser)
        download.get(base_url)
        ele = download.check_box
        for i in range(4):
            ele[i].click()
        download.down_all.click()
        sleep(1)
        download.hyper.click()
        sleep(1)
        download.batch_download.click()

    def test_download_file_pure(self, browser, base_url):
        """
        批量下载纯净版
        """
        download = DownloadFile(browser)
        download.get(base_url)
        ele = download.check_box
        for i in range(4):
            ele[i].click()
        download.down_all.click()
        sleep(1)
        download.pure.click()
        sleep(1)
        download.batch_download.click()


        sleep(5)



if __name__ == '__main__':
    pytest.main(["-v", "-s", "./test_05_download_all.py"])
