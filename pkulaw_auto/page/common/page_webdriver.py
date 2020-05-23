import time
class WebDriver(object):
    def __init__(self,driver):
        self.driver = driver

    def wait(self,sec):
        time.sleep(sec)

    def get_title(self):
        return self.driver.title

    def get_alert_text(self):
        return self.driver.swith_to.alert.text

    def accept_alert(self):
        return self.driver.swith_to.alert.accept()

    def swith_to_fram_out(self):
        self.driver.swith_to.default_content()
