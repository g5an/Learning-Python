#encoding:utf-8
#模拟打开浏览器，下载文件
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://192.168.31.31/itmm/index.php')
#获取登陆窗口
# eg:<input type="text" id="name" name="name" value="" class="form-control" placeholder="Username">
username=browser.find_element_by_id('name')
#username=browser.find_element_by_name('name')
#username=browser.find_element_by_tag_name()
#username=borwser.fine_element_by_xpath('//*[@id="name"]')
username.clear()
username.send_keys('admin')
password=browser.find_element_by_id('password')
password.clear()
password.send_keys('admin')
#获取登陆按钮并点击
dl=browser.find_element_by_id('enter').click()
#等待几秒
browser.implicitly_wait(2)
browser.get('http://192.168.31.31/itmm/srv_status.php?ddreset=1')
cl2=browser.find_element_by_id('excelOut').click()
#browser.get('http://192.168.31.31/itmm/srv_status.php?export=execl&fullscreen=0&period=today')
