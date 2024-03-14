# 用 selenium + edge 模拟浏览器访问
# driver.page_source 获取源码

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# 使用 EdgeChromiumDriverManager 自动管理驱动程序
service = Service(EdgeChromiumDriverManager().install())    # 下载最新驱动
driver = webdriver.Edge(service=service)

driver.get('https://www.baidu.com')                         # 访问页面
time.sleep(8)

print(driver.page_source)
print('\n\n[+] url: ',driver.current_url,'\n')
