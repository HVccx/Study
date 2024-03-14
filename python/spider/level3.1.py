#编写一个爬虫程序，从网站 https://www.amazon.com/ 上获取所有图书的信息，并将其保存到数据库中。您需
#要获取每本书的名称、作者、价格和评论数量。注意，Amazon网站采用动态加载的方式渲染页面内容，因此您可
#能需要使用Selenium等工具来模拟浏览器行为。
#您可以使用Python的Selenium库来模拟浏览器行为，并使用BeautifulSoup来解析HTML内容。为了保存数据到数
#据库，您可以选择使用MySQL、SQLite或其他数据库系统，并设计合适的数据库表结构来存储图书信息。

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

proxy = '127.0.0.1:7890'
url = 'https://www.amazon.com/b?node=283155'
i = 1

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-web-security")  # 禁用同源策略
chrome_options.add_argument("--disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure,StrictOriginIsolation")  # 禁用第三方cookie的限制
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 隐藏Selenium的自动化标志
chrome_options.add_argument('--proxy-server=http://' + proxy)   # 设置代理
chrome_options.add_argument('--headless')  # 无头模式，不打开浏览器窗口

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)                     # 第一次请求没有内容
time.sleep(4)
driver.refresh()                    # 刷新页面
time.sleep(5)

# 模拟滚动页面，加载更多图书
scroll_distance = 200               # 设置滚动距离
for i in range(40):
    driver.execute_script(f"window.scrollTo(0,{scroll_distance*(i + 1)});")
    time.sleep(.5)                   # 每三秒向下滚动 500 像素

print(len(driver.page_source))      # 输出内容长度

# 将页面源码写入 test.html 文件
with open("amazon_books.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)  # 写入文件 test.html 中



soup = BeautifulSoup(driver.page_source, 'html.parser')
books = soup.find_all('div', class_='p13n-sc-uncoverable-faceout')

for book in books:
    
    price_span = book.find('span', class_='_cDEzb_p13n-sc-price_3mJ9Z')
    price = price_span.text.strip() if price_span else '未知价格'

    spans = book.find_all('span', class_='a-size-small')

    title = spans[0].text.strip() if spans[0] else '未找到标题'
    if len(spans) >= 2:
        review_count_span = spans[1]
        review_count = review_count_span.text.strip()
    else:
        review_count = '未知评论数'

    #title_span = book.find('span', class_='a-size-small')
    #title = title_span.text.strip() if title_span else '未找到标题'

    #review_count_span = book.find('span', class_='a-size-small')
    #review_count = review_count_span.text.strip() if title_span else '未知评论数'

    print(i)
    i += 1
    print(f'[+] Title: {title}')
    print(f'[+] Price: {price}')
    print(f'[+] Review count: {review_count}')
    print('\n---\n')

driver.quit()
