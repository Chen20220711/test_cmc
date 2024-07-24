import time

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
pw.send_keys("windit778489")

#定位登录按钮元素
bt=wd.find_element(By.CLASS_NAME,"login_btns")#此处的类名是div的类名，不是button的类名
#用WebDriver对象的click方法操纵登录按钮
bt.click()

#验证是否登录成功
#assert "白月销售管理系统" in wd.title

#WebDriver对象有window_handles 属性，这是一个列表对象， 里面包括了当前浏览器里面所有的窗口句柄
for window in wd.window_handles:  # 获取当前所有的浏览器窗口句柄，并遍历
    wd.switch_to.window(window)  # 逐个切换窗口句柄，括号里面是遍历过得窗口句柄
    if "home" in wd.current_url:  # 判断当前浏览器窗口是否含有目标关键字“customers”，webdriver对象获取当前网页的网址
        break
#点击系统管理0
wd.find_element(By.CSS_SELECTOR,"li[class=aside-item]>a").click()

#点击数字双胞胎
wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/ul/li[2]").click()

#点击总貌图设置
wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/ul/li[3]").click()

#点击上下级设置
wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/ul/li[4]").click()



#点击账户设置
wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/ul/li[5]").click()



# 这里加入等待用户输入，防止闪退
input('等待回车键结束程序')