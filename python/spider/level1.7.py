# 爬取 json 格式数据并处理
# 用 json.loads 将 json 转换成 字典 或 其他类型; json.dump 将 字典 转换成 json

import requests
import json
import jsonpath_ng

url = 'https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=30'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)
print(len(response.text))



# 把 json 格式字符串转换成 字典 或 其他类型（这里为 list ）
res = json.loads(response.text)
print(type(res))

for i in range(30):
    print(f'[{i+1}]: ',res[i]['title'])



# 下面为处理 list 的方法，若处理 字典（name = jsonpath_ng(res, '$..title')）
name = [match.value for match in jsonpath_ng.parse('$..title').find(res)]
print(name)