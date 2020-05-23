import yagmail
from config import RunConfig


def sendemail(report,sendmail_address,sendmail_password,receivemail_address,email_host):

    #邮箱服务器：发送用户名，密码，服务器
    yag = yagmail.SMTP(user = sendmail_address,password = sendmail_password,host = email_host)

    #邮件内容
    contents = ["法宝登录测试报告","测试报告如下："]

    #发送邮件:接收人（用list添加多个接收人），标题，内容,附件（用list发送多个附件）
    #report_file = 'D:\\2020_03_01_19_10_45_report.html'
    return  yag.send(receivemail_address," 法宝登录测试报告",contents,[report])


