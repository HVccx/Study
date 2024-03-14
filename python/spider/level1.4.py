# 用 selenium + chrome 爬取网页
# 需要 clash 开启系统代理下载驱动器
# 通过 service 选项传入驱动器

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

proxy = '127.0.0.1:7890'                                        # 设置代理
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)

# 使用 Service 对象和 ChromeDriverManager 自动管理驱动程序
service = Service(ChromeDriverManager().install())              # 下载最新驱动器
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://github.com')                                # 访问页面
time.sleep(8)

print(driver.page_source)
print('\n\n[+] url: ',driver.current_url,'\n')

driver.quit()