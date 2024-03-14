#编写一个爬虫程序，爬取 https://www.amazon.com/ 的源代码，要包含尽量多的图书信息

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from retrying import retry          # 遇到报错时尝试多次

proxy = '127.0.0.1:7890'
url = 'https://www.amazon.com/b?node=283155'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-web-security")  # 禁用同源策略
chrome_options.add_argument("--disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure,StrictOriginIsolation")  # 禁用第三方cookie的限制
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 隐藏Selenium的自动化标志
chrome_options.add_argument('--proxy-server=http://' + proxy)   # 设置代理
#chrome_options.add_argument('--headless')  # 无头模式，不打开浏览器窗口

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)                     # 第一次请求没有内容
time.sleep(3)
driver.refresh()                    # 刷新页面
time.sleep(5)

# 模拟滚动页面，加载更多图书
scroll_distance = 100               # 设置滚动距离
for i in range(60):
    driver.execute_script(f"window.scrollTo(0,{scroll_distance*(i + 1)});")
    time.sleep(.5)                   # 每三秒向下滚动 500 像素

print(len(driver.page_source))      # 输出内容长度

# 将页面源码写入 test.html 文件
with open("amazon_books.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)  # 写入文件 test.html 中

driver.quit()