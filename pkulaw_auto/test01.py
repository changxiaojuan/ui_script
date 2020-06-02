from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.pkulaw.com")
sleep(2)

driver.find_element_by_id("newloginbtn").click()

driver.find_element_by_id("inputUserName").send_keys("csgr")
driver.find_element_by_id("inputPwd").send_keys("bdyh@2019")

driver.find_element_by_id("loginByUserName").click()
sleep(2)

ele = driver.find_elements_by_name("recordList")
sum = 0
for i in range(4):
    ele[i].click()
driver.find_element_by_class_name("down-all").click()
sleep(2)
driver.find_element_by_id("tool-word").click()

driver.find_element_by_id("batchDownload").click()
