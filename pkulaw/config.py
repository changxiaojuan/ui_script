

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./test_case/"


    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    url = "https://www.pkulaw.com/"
    username = "csgr"
    password = "bdyh@2019"

    #配置邮件发送
    host = "smtp.chinalawinfo.com"
    sendmail_address = "changxiaojuan@chinalawinfo.com"
    sendmail_password = "bdyh@2013"
    receivemail_address = ["changxiaojuan@chinalawinfo.com","505734704@qq.com"]

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"


