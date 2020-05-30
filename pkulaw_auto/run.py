import pytest
from config import RunConfig
import time,os
from conftest import REPORT_DIR
from send_email import sendemail


sendmail_address = RunConfig.sendmail_address
sendmail_password = RunConfig.sendmail_password
receivemail_address = RunConfig.receivemail_address
email_host = RunConfig.host

def report_dir(now_time):
    """
    初始化测试报告目录
    """
    os.mkdir(REPORT_DIR + now_time)
    os.mkdir(REPORT_DIR + now_time + "/image")




if __name__ == '__main__':
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_dir(now_time)
    report = os.path.join(REPORT_DIR, now_time, "report.html")

    #pytest.main(["-v","-s",RunConfig.cases_path,"--html="+report])
    pytest.main(["-v", "-s", "./test_case/", "--html=" + report])
    #sendemail(report,sendmail_address,sendmail_password,receivemail_address,email_host)
