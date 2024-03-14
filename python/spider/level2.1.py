# 抓取豆瓣电影Top250榜单的每一页，提取每部电影的排名、电影名称...，并将这些信息写入到名为douban_top250.csv的CSV文件中
# 需要 header 欺骗
# 用 BeautifulSoup 的 find 方法查找第一个 find_all 查找全部
# format() 替换，{} 为占位符

import requests
from bs4 import BeautifulSoup
import csv
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

def scrape_douban_top250(url):
    # 创建CSV文件并写入表头
    with open('douban_top250.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['排名', '电影名称', '评分', '导演', '主演', '上映日期', '简介'])

        # 循环遍历每一页
        for page in range(10):
            # 发送HTTP GET请求
            response = requests.get(url.format(page * 25),headers=headers)
            response.encoding = 'utf-8'
            print('\n[+]URL: ',response.url,'\tstatus: ',response.status_code)
            time.sleep(2)

            # 解析HTML内容
            soup = BeautifulSoup(response.text, 'html.parser')

            # 提取电影信息
            items = soup.find_all('div', class_='item')
            for item in items:
                ranking = item.find('em').text
                title = item.find('span', class_='title').text
                rating = item.find('span', class_='rating_num').text
                info = item.find('p').text.strip().split('\n')
                director = info[0].split('导演: ')[1].split('主演: ')[0]
                actors = info[0].split('主演: ')[-1]
                date = info[1].split('/')[0].strip()
                summary = item.find('span', class_='inq').text if item.find('span', class_='inq') else ''
                
                # 将电影信息写入CSV文件
                writer.writerow([ranking, title, rating, director, actors, date, summary])

# 豆瓣电影Top250榜单URL模板
if __name__ == '__main__':
    url_template = 'https://movie.douban.com/top250?start={}'
    scrape_douban_top250(url_template)
