from selenium import webdriver
from selenium.webdriver.common.by import By
#创建浏览器驱动对象
wd = webdriver.Chrome()
#等待服务器返回数据
wd.implicitly_wait(10)
#打开网址
wd.get("http://10.100.50.203:8087/CMC/index.html?v3.1.27.019#/login")#此处要指明完整的url，不止i和端口

#定位用户名框、密码框元素
ur=wd.find_element(By.ID,"user-name")
pw=wd.find_element(By.ID,"pass_word")
#操纵用户名框、密码框，输入用户名、密码
ur.clear()
pw.clear()
ur.send_keys("admin")
pw.send_keys("windit1124478")

#定位登录按钮元素
bt=wd.find_element(By.CLASS_NAME,"login_btns")#此处的类名是div的类名，不是button的类名
#用WebDriver对象的click方法操纵登录按钮
bt.click()

#验证是否登录成功
#assert "白月销售管理系统" in wd.title
# 这里加入等待用户输入，防止闪退
input('等待回车键结束程序')

#关闭浏览器
#wd.quit()



