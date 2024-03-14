# 以clash为代理爬取被墙网页

import requests
from bs4 import BeautifulSoup
import time

# 要爬取的网页URL
url = 'https://github.com'

def simple_crawler(url):
    # 发送HTTP GET请求，并添加header参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
    }
    response = requests.get(url, headers=headers, proxies=proxies)

    # 检查响应状态码是否为200（表示成功）
    if response.status_code == 200:
        # 使用Beautiful Soup解析HTML内容
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 在这里可以根据网页结构提取所需信息
        # 这里只是简单地打印标题
        print("\npage:",response.text)
        print("\n[+]status_code:",response.status_code)
        print("\n[+]Title:", soup.title.text)
        time.sleep(2)
        
    else:
        print("Failed to fetch the page.\nX.X")


if __name__ == '__main__':
    simple_crawler(url)
