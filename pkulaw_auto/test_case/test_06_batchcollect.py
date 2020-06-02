from page.page_06_batchcollect import BatchCollect
from  time import sleep

class TestBatchCollect():
    def test_batch_collect(self,browser,base_url,username,password):
        batchcollect = BatchCollect(browser)
        batchcollect.get(base_url)
        ele = batchcollect.check_box
        for i in range(4):
            ele[i].click()
        sleep(1)
        batchcollect.batch_collect.click()
        if batchcollect.login_btn:
            # 如果未登录则先登录
            sleep(1)
            batchcollect.login_btn.click()
            sleep(2)
            batchcollect.username.send_keys(username)
            batchcollect.password.send_keys(password)
            batchcollect.remember.click()
            batchcollect.login.click()
            sleep(2)
            ele = batchcollect.check_box
            for i in range(4):
                ele[i].click()
            batchcollect.batch_collect.click()
            sleep(5)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "./test_06_batchcollect.py"])