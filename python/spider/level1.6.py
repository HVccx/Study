# 爬取图片 并 保存

import requests

url = 'https://cdn.oaistatic.com/_next/static/media/favicon-32x32.be48395e.png'

respones = requests.get(url)
print(respones.content)

with open('chatGPT.png', 'wb') as file:
    file.write(respones.content)