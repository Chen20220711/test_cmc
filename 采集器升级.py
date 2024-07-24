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
ur.send_keys("chentt")
pw.send_keys("123456")

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


#点击采集器升级
wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/ul[1]/li[7]/a").click()


input1=wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/input")
input1.send_keys(r'F:\项目\V1.0.34.0.dgm')

"""
1.通常，网站页面上传文件的功能，是通过 type 属性 为 file 的 HTML input 元素实现的。
<input type="file" multiple="multiple">
使用selenium自动化上传文件，我们只需要定位到该input元素，然后通过 send_keys 方法传入要上传的文件路径即可。
# 先定位到上传文件的 input 元素
ele = wd.find_element(By.CSS_SELECTOR, 'input[type=file]')

# 再调用 WebElement 对象的 send_keys 方法
ele.send_keys(r'h:\g02.png')
"""

#上传成功，点击确认
#wd.switch_to.alert.accept()
#sure=wd.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/button")
#sure.click()


#上传失败，点击确认
sure=wd.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/button")
sure.click()


#点击版本
wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[6]/td[1]").click()

#点击采集器
wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[1]").click()


#点击升级采集器
wd.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/button").click()


"""
2.弹出的对话框有三种类型，分别是 Alert（警告信息）、confirm（确认信息）和prompt（提示输入）
3.有些弹窗并非浏览器的alert弹窗，而是页面的html元素，这种对话框只需要按照常规方法定位元素就行
"""


# 这里加入等待用户输入，防止闪退
input('等待回车键结束程序')