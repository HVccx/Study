# 从维基百科（https://zh.wikipedia.org/wiki/Wikipedia:首页）中获取以下信息并保存到文本文件中：
# 1、维基百科首页的标题
# 2、维基百科首页的简介内容
# 代理绕过限制
# 

import requests
from bs4 import BeautifulSoup
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
    }

def scrape(url):
    # 创建CSV文件并写入表头

    response = requests.get(url,headers=headers, proxies=proxies)
    response.encoding = 'utf-8'
    print('\n[+]URL: ',response.url,'\tstatus: ',response.status_code)
    time.sleep(2)

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取首页标题和简介内容
    title = soup.find('h1', id='firstHeading').text
    intro = soup.find('div', id='column-tips').p.text # id='column-tips'    class_='plainlinks mp-2012-text'

    # 将标题和简介内容保存到文本文件中
    with open('wikipedia_homepage.txt', 'w', encoding='utf-8') as file:
        file.write(f'标题：{title}\n\n')
        file.write(f'简介：{intro}')
            

if __name__ == '__main__':
    url_template = 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5'
    scrape(url_template)
