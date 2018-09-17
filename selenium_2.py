#!/bin/bash
#后台静默打开一个虚拟窗口，静默下载完成退出。
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()
#设置Firefox默认的下载地址，屏蔽特定类型的文件不弹窗
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', '/usr/local/src/test/')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/vnd.ms-excel')

browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://192.168.31.31/itmm/index.php')
username=browser.find_element_by_id('name')
username.clear()
username.send_keys('admin')
password=browser.find_element_by_id('password')
password.clear()
password.send_keys('admin')
cl=browser.find_element_by_id('enter').click()
print(browser.title)

browser.get('http://192.168.31.31/itmm/srv_status.php?ddreset=1')
cl2=browser.find_element_by_id('excelOut').click()
browser.implicitly_wait(5)
browser.quit()
display.stop()